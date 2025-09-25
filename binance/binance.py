#import os
import requests                       #> pip instal requests
import psycopg2
from datetime import datetime
from zoneinfo import ZoneInfo         #> pip install zoneinfo

#psql_password = os.getenv("PSQL_PASSWORD")
psql_password = 12345678
#if not psql_password:   > Eğer ortam değişkeni ayarlanmadıysa hata verir
#    raise ValueError("PSQL_PASSWORD environment variable is not set!")

db_config = {
    "host": "localhost",
    "port": 5432,
    "database": "postgres",
    "user":  "postgres",
    "password": 12345678
}

symbols = [
    "BTCUSDT", "ETHUSDT", "BCCUSDT", "NEOUSDT", "LTCUSDT", "QTUMUSDT", "ADAUSDT",
    "XRPUSDT", "EOSUSDT", "TUSDUSDT", "IOTAUSDT", "XLMUSDT", "ONTUSDT", "TRXUSDT",
    "ETCUSDT", "ICXUSDT", "VENUSDT", "NULSUSDT", "VETUSDT", "PAXUSDT", "BCHABCUSDT",
    "BCHSVUSDT", "USDCUSDT", "LINKUSDT", "WAVESUSDT", "BTTUSDT", "USDSUSDT", "ONGUSDT",
    "HOTUSDT", "ZILUSDT", "ZRXUSDT", "FETUSDT", "BATUSDT", "XMRUSDT", "ZECUSDT",
    "IOSTUSDT", "CELRUSDT", "DASHUSDT", "NANOUSDT", "OMGUSDT", "THETAUSDT",
    "ENJUSDT", "MITHUSDT", "MATICUSDT", "ATOMUSDT", "TFUELUSDT", "ONEUSDT",
    "FTMUSDT", "ALGOUSDT"
]

binance_api_url = "https://api.binance.com/api/v3/ticker/price"

try:
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    for symbol in symbols:
        response = requests.get(binance_api_url, params={"symbol": symbol})

        if response.status_code == 200:
            data = response.json()
            name = data['symbol']
            price = float(data['price'])
            now = datetime.now(ZoneInfo("Europe/Istanbul"))
            cursor.execute("""
                INSERT INTO tbl_binance2_staj (name, price, binancetime)
                VALUES (%s, %s, %s);
            """, (name, price, now))

            print(f"[✓] {name} verisi eklendi: {price}")
        elif response.status_code == 401:
            print(f"[!] {symbol}: Yetkisiz erişim (401). API kimlik doğrulaması gerekebilir.")
        elif response.status_code == 429:
            print(f"[!] {symbol}: Çok fazla istek atıldı (429). Rate limit'e takıldınız.")
        elif 500 <= response.status_code < 600:
            print(f"[!] {symbol}: Binance sunucusu hatası ({response.status_code}).")
        else:
            print(f"[!] {symbol}: Beklenmeyen durum kodu: {response.status_code}")

    conn.commit()
    print("Tüm Veriler İşleme Alındı.")

except Exception as e:
    print("Hata:", e)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
