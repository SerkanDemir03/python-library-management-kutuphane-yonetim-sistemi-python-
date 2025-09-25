import math
import logging

logging.basicConfig(
 filename="ogrenci_sistemi.log",
 filemode="a",
 encoding="utf-8",
 level=logging.INFO,
 format=" %(message)s"
)
def ogrenci_veri (ogr_no):
#Ogrenci bilgileri ekliyoruz
 ad_soyad = input("Ogrenci Ad Ve Soyadını Giriniz : ")
 yas = input("Ogrenci Yasını Giriniz : ")
 while True:
  ogrenci_notlar = input("Notları virgülle giriniz (örn: 50,60,70): ")
  if "," not in ogrenci_notlar:
   print("Lütfen notları virgül ile ayırın (örn: 50,60,70).")
   continue
  parts = [x.strip() for x in ogrenci_notlar.split(",")]
  if len(parts) != 3:
   print("Eksik girdiniz. 3 tane not giriniz (örn: 50,60,70).")
   continue
  try:
   notlar = tuple(int(x) for x in parts)
  except ValueError:
   print("Yanlış değer girdiniz. Lütfen sadece sayı giriniz (örn: 50,60,70).")
   continue
  deger_araligi_hatasi = False
  for g in notlar:
   if g < 0:
    print("Not 0'dan küçük olamaz:", g)
    deger_araligi_hatasi = True
    break
   elif g > 100:
    print("Not 100'den büyük olamaz:", g)
    deger_araligi_hatasi = True
    break
  if deger_araligi_hatasi:
   continue
  print("Notlar:", notlar)
  break

# Ortalama hesapla: 30% vize, 30% final, 40% proje
 ogrenci_ortalamasi = 0.3 * notlar[0] + 0.3 * notlar[1] + 0.4 * notlar[2]
 
# Minimum notu bul
 min_not = min(notlar)
#Maximum notu bul
 max_not =max(notlar)

 print("------------------------------------------------------------------------------")
 print(f"{ogr_no}. Öğrenci: {ad_soyad} ")
 print(f"Notlar (Vize, Final, Proje): {ogrenci_notlar}")
 print(f"Ortalama: {ogrenci_ortalamasi:.2f}")
 print(f"En Düşük Not: {min_not}")
 print(f"En Yüksek Not: {max_not} ")
 logging.info(
  f"OgrenciEkle no={ogr_no}, ad='{ad_soyad}', yas='{yas}', notlar='{ogrenci_notlar}', ortalama={ogrenci_ortalamasi:.2f}, min={min_not}, max={max_not}"
 )
 return ogrenci_ortalamasi

ogrenci_sayisi = 0
toplam_ortalama = 0.0

while True :
     secim =input("Ogrenci Eklemek İstiyor Musunuz ? (E/H)" )
     if secim== "E" or secim=="e":
      
        ogrenci_sayisi += 1
        ortalama = ogrenci_veri (ogrenci_sayisi)
        toplam_ortalama += ortalama
     elif secim=="H" or secim=="h" :
      
        print(f"Toplam eklenen öğrenci sayısı: {ogrenci_sayisi}")
        if ogrenci_sayisi > 0:
          genel_ortalama = toplam_ortalama / ogrenci_sayisi
          print(f"Genel Not Ortalaması: {genel_ortalama:.0f}")
          logging.info(
           f"Cikis : toplam_ogrenci={ogrenci_sayisi}, genel_ortalama={genel_ortalama:.2f}"
          )
        else:
          logging.info(
           "Cikis toplam_ogrenci=0"
          )
        print("Cıkılıyor..." )
        break

     else :
       print("Gecersiz Bir Deger Girdiniz Lutfen 'E' Veya 'H' giriniz.")
       logging.warning(f"GecersizSecim girilen='{secim}'")




