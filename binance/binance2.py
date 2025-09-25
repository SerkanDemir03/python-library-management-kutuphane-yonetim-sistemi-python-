import os
import requests
import psycopg2
from datetime import datetime
from zoneinfo import ZoneInfo
import time

# Şifre ortam değişkeninden alınır
#psql_password = os.getenv("PSQL_PASSWORD")
#if not psql_password:
#    raise ValueError("PSQL_PASSWORD environment variable is not set!")
psql_password = 12345678
# Veritabanı yapılandırması
db_config = {
    "host": "localhost",
    "port": 5432,
    "database": "binance",
    "user":  "postgres",
    "password": psql_password
}

# Hedeflenen semboller kümesi
symbols = {
    "BTCUSDT", "ETHUSDT", "BCCUSDT",  "NEOUSDT", "LTCUSDT", "QTUMUSDT", "ADAUSDT",
    "XRPUSDT", "EOSUSDT", "TUSDUSDT", "IOTAUSDT", "XLMUSDT", "ONTUSDT", "TRXUSDT",
    "ETCUSDT", "ICXUSDT", "VENUSUSDT", "NULSUSDT", "VETUSDT", "PAXUSDT", "BCHABCUSDT",
    "BCHSVUSDT", "USDCUSDT", "LINKUSDT", "WAVESUSDT", "BTTUSDT", "USDSUSDT", "ONGUSDT",
    "HOTUSDT", "ZILUSDT", "ZRXUSDT",    "FETUSDT", "BATUSDT", "XMRUSDT", "ZECUSDT",
    "IOSTUSDT", "CELRUSDT", "DASHUSDT", "NANOUSDT", "OMGUSDT", "THETAUSDT",
    "ENJUSDT", "MITHUSDT", "MATICUSDT", "ATOMUSDT", "TFUELUSDT", "ONEUSDT",
    "FTMUSDT", "ALGOUSDT"
}

binance_api_url = "https://api.binance.com/api/v3/ticker/price"

def binance_data():
    try:
        # Veritabanı bağlantısı
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        # Binance API çağrısı
        response = requests.get(binance_api_url)
        #get > veriyi çekmek için
        #post > veri yazmak için
        #delete > veri silmek için
        #put / update > veri güncellemek için    

        #200 > başarılı
        #401 > yetkisiz erişim

        if response.status_code != 200:
            raise Exception(f"Binance API hatası: {response.status_code}")

        now = datetime.now(ZoneInfo("Europe/Istanbul"))
        all_data = response.json()

        # Toplu veri listesi hazırlanıyor
        bulk_insert_data = [
            (item["symbol"], float(item["price"]), now)
            for item in all_data
            # if item["symbol"] in symbols
        ]

        # Boş değilse veritabanına topluca yaz
        if bulk_insert_data:
            cursor.executemany("""
                INSERT INTO tbl_binance (name, fiyat, binancetime)
                VALUES (%s, %s, %s)
            """, bulk_insert_data)

            conn.commit()
            print(f"Toplam {len(bulk_insert_data)} veri başarıyla eklendi.")
        else:
            print("Uygun sembol bulunamadı, ekleme yapılmadı.")

    except Exception as e:
        print("Hata:", e)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()



def main():
    while True:
        binance_data()
        time.sleep(3)
        
if __name__ == "__main__":
    main()