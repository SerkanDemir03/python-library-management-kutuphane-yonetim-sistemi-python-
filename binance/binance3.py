import os
import requests
import psycopg2
from datetime import datetime
from zoneinfo import ZoneInfo
import time

# Şifre ortam değişkeninden alınır
psql_password = os.getenv("PSQL_PASSWORD") or "12345678"
desired_symbols_env = os.getenv("BINANCE_SYMBOLS")  # ör: "BTCUSDT,ETHUSDT,XRPUSDT"
desired_quote_env = os.getenv("BINANCE_QUOTE")  # ör: "USDT"
positions_symbols_env = os.getenv("POSITIONS_SYMBOLS")  # ör: "BTCUSDT,ETHUSDT" (P&L raporu için filtre)

# Veritabanı yapılandırması
db_config = {
    "host": "localhost",
    "port": 5432,
    "database": "denemedb",
    "user":  "postgres",
    "password": psql_password
}

# Anlık fiyat endpoint'i: sembol başına güncel fiyat döner
binance_api_url = "https://api.binance.com/api/v3/ticker/price"

# Yardımcı: database yoksa bir defa oluştur
def quote_ident_pg(identifier: str) -> str:
    return '"' + identifier.replace('"', '""') + '"'

def ensure_database_exists(cfg: dict) -> None:
    # Her zaman 'postgres' db'sine bağlan, hedef DB yoksa oluştur
    admin_cfg = dict(cfg)
    admin_cfg["database"] = "postgres"
    dbname = cfg["database"]
    try:
        with psycopg2.connect(**admin_cfg) as admin_conn:
            admin_conn.autocommit = True
            with admin_conn.cursor() as c:
                c.execute("SELECT 1 FROM pg_database WHERE datname = %s", (dbname,))
                exists = c.fetchone() is not None
                if not exists:
                    print(f"Veritabanı oluşturuluyor: {dbname}")
                    c.execute(f"CREATE DATABASE {quote_ident_pg(dbname)}")
                else:
                    print(f"Veritabanı mevcut: {dbname}")
    except Exception as e:
        print(f"Veritabanı kontrol/oluşturma hatası: {e}")

try:
    ensure_database_exists(db_config)
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    # Yardımcı: identifier kaçışlama
    def qi(identifier: str) -> str:
        return '"' + identifier.replace('"', '""') + '"'

    print("Başlatıldı. İlk sorgu hemen, ardından her 60 saniyede yinelenecek.")

    # HTTP oturumunu yeniden kullanmak için
    http = requests.Session()
    http.headers.update({"Connection": "keep-alive"})

    # Kayıtları tutacağımız tablo: id, name, price, time
    table_name = "coin_prices"
    try:
        cursor.execute(
            f"""
                CREATE TABLE IF NOT EXISTS {qi(table_name)} (
                    id SERIAL PRIMARY KEY,
                    {qi('name')} TEXT NOT NULL,
                    {qi('price')} NUMERIC NOT NULL,
                    {qi('time')} TIMESTAMPTZ NOT NULL
                )
            """
        )
        cursor.execute(
            f"""
                CREATE INDEX IF NOT EXISTS {qi(table_name + '_name_idx')}
                ON {qi(table_name)} ({qi('name')})
            """
        )
        cursor.execute(
            f"""
                CREATE INDEX IF NOT EXISTS {qi(table_name + '_name_time_idx')}
                ON {qi(table_name)} ({qi('name')}, {qi('time')} DESC)
            """
        )
        # Pozisyon tablosu: alınan coin'ler ve maliyetler
        cursor.execute(
            f"""
                CREATE TABLE IF NOT EXISTS {qi('positions')} (
                    id SERIAL PRIMARY KEY,
                    {qi('name')} TEXT NOT NULL,
                    {qi('buy_price')} NUMERIC NOT NULL,
                    {qi('quantity')} NUMERIC NOT NULL,
                    {qi('buy_time')} TIMESTAMPTZ NOT NULL DEFAULT NOW()
                )
            """
        )
        cursor.execute(
            f"""
                CREATE INDEX IF NOT EXISTS {qi('positions_name_idx')}
                ON {qi('positions')} ({qi('name')})
            """
        )
        conn.commit()
    except Exception as idx_err:
        print(f"Tablo/index oluşturma sırasında hata: {idx_err}")
        conn.rollback()

    while True:
        try:
            response = http.get(binance_api_url, timeout=10)
            response.raise_for_status()
            print(response.status_code)
        except requests.RequestException as req_err:
            print(f"API isteği başarısız: {req_err}")
            time.sleep(10)
            continue

        all_data = response.json()
        now = datetime.now(ZoneInfo("Europe/Istanbul"))

        # İstenilen sembol/quote filtreleri
        # İzlenecek semboller
        if desired_symbols_env:
            desired_symbols = set(s.strip().upper() for s in desired_symbols_env.split(',') if s.strip())
        else:
            # Varsayılan geniş liste (binance2.py'den)
            desired_symbols = {
                "BTCUSDT", "ETHUSDT", "BCCUSDT", "NEOUSDT", "LTCUSDT", "QTUMUSDT", "ADAUSDT",
                "XRPUSDT", "EOSUSDT", "TUSDUSDT", "IOTAUSDT", "XLMUSDT", "ONTUSDT", "TRXUSDT",
                "ETCUSDT", "ICXUSDT", "VENUSDT", "NULSUSDT", "VETUSDT", "PAXUSDT", "BCHABCUSDT",
                "BCHSVUSDT", "USDCUSDT", "LINKUSDT", "WAVESUSDT", "BTTUSDT", "USDSUSDT", "ONGUSDT",
                "HOTUSDT", "ZILUSDT", "ZRXUSDT", "FETUSDT", "BATUSDT", "XMRUSDT", "ZECUSDT",
                "IOSTUSDT", "CELRUSDT", "DASHUSDT", "NANOUSDT", "OMGUSDT", "THETAUSDT",
                "ENJUSDT", "MITHUSDT", "MATICUSDT", "ATOMUSDT", "TFUELUSDT", "ONEUSDT",
                "FTMUSDT", "ALGOUSDT"
            }
        desired_quote = desired_quote_env.strip().upper() if desired_quote_env else None

        # Bu turda gelen verileri tekil kayıtlar olarak tabloya ekle
        insert_sql = f"""
            INSERT INTO {qi(table_name)} ({qi('name')}, {qi('price')}, {qi('time')})
            VALUES (%s, %s, %s)
        """

        to_insert_rows = []
        for item in all_data:
            symbol = item.get("symbol")
            price_str = item.get("price")
            if not symbol or price_str is None:
                continue

            symbol = symbol.upper()
            if desired_symbols and symbol not in desired_symbols:
                continue
            if desired_quote and not symbol.endswith(desired_quote):
                continue

            try:
                price_val = float(price_str)
            except (ValueError, TypeError):
                continue

            to_insert_rows.append((symbol, price_val, now))

        if to_insert_rows:
            cursor.executemany(insert_sql, to_insert_rows)
        conn.commit()
        print(f"Kaydedilen kayıt sayısı: {len(to_insert_rows)}")

        # XRPUSDT için güncel (çalışma süresi) min/max değerlerini göster
        # Panel: P&L raporu (positions tablosundaki coinler için)
        # İsteğe bağlı filtre: POSITIONS_SYMBOLS
        positions_filter = None
        if positions_symbols_env:
            positions_filter = set(s.strip().upper() for s in positions_symbols_env.split(',') if s.strip())

        try:
            # En son fiyatlarla birlikte P&L hesapla
            cursor.execute(
                f"""
                    SELECT p.{qi('name')}, p.{qi('buy_price')}, p.{qi('quantity')},
                           cp.{qi('price')} AS last_price, cp.{qi('time')} AS last_time
                    FROM {qi('positions')} p
                    JOIN LATERAL (
                        SELECT {qi('price')}, {qi('time')}
                        FROM {qi(table_name)}
                        WHERE {qi('name')} = p.{qi('name')}
                        ORDER BY {qi('time')} DESC
                        LIMIT 1
                    ) cp ON TRUE
                """
            )
            rows = cursor.fetchall()
            print("P&L Raporu:")
            for name, buy_price, qty, last_price, last_time in rows:
                if positions_filter and name not in positions_filter:
                    continue
                try:
                    buy_price_f = float(buy_price)
                    qty_f = float(qty)
                    last_price_f = float(last_price)
                except (TypeError, ValueError):
                    continue
                pnl = (last_price_f - buy_price_f) * qty_f
                pnl_pct = ((last_price_f / buy_price_f) - 1.0) * 100.0 if buy_price_f else 0.0
                print(f"  {name}: last={last_price_f:.6f} qty={qty_f} pnl={pnl:.2f} ({pnl_pct:.2f}%) time={last_time}")
        except Exception as pnl_err:
            print(f"P&L hesaplama hatası: {pnl_err}")

        time.sleep(60)

except KeyboardInterrupt:
    print("Döngü kullanıcı tarafından durduruldu.")

except Exception as e:
    print("Hata:", e)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
