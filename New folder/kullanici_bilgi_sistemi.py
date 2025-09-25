import sys
import platform
from timeit import default_timer
from tkinter import N
print("Merhaba, Kullanıcı Bilgi Sistemine Hoşgeldiniz!")#kullanıcı bilgi sistemi başladı.
print("Python Version:", platform.python_version())#python versiyonu bilsinini kısaca verir.

ad_soyad = input("Adınızı Soyadınızı Giriniz: ")#kullanıcı adı ve soyadı girdisi
yas = int(input("Yasınızı Giriniz: "))#kullanıcı yaşı girdisi
maas = float(input ("Maasınızı Giriniz:"))#kullanıcı maası girdisi
ogrenci_mi = input("Öğrenci Mi? (True/False):")#kullanıcı öğrenci mi girdisi
cevap =bool(ogrenci_mi.lower())#kullanıcı öğrenci mi girdisi boolean değere çevrildi
#yukarıda ogrenci_mi sorusunu sorarken str türünü boolean değere çevirdigi ıcın false bile verse true cıkar 
#kullanıcıdan veri alarak dogruluga göre yapsaydık  cevap =bool(ogrenci_mi.lower()) yerine alttaki kontrol bloklarını yazmamız gerekirdi.
"""
if ogrenci_mi == "true":
    cevap = True
elif ogrenci_mi== "false":
    cevap = False
else:
    print("Geçersiz giriş!")
    cevap = None
"""
    
adres = None # Kullanıcıdan veri almadan None olarak tanımlanmıs adres_bilgisi .
"""
# Kullanıcıdan veri alarak yaparsak alttaki kod bloklarını kullanmamız daha dogru olacaktır.
adres_bilgisi = input("Adresinizi giriniz (boş bırakabilirsiniz): ")#kullanıcı adresi girdisi
adres = adres_bilgisi if adres_bilgisi else None #kullanıcı adresi girdisi boş bırakılırsa None değeri atanır
"""
print("--------------------------------")
print("Kullanıcı Ad Ve Soyadı : ", ad_soyad)#kullanıcı adı ve soyadı yazdırılır
print("Kullanıcı Yaşı : ", yas) #kullanıcı yaşı yazdırılır
print("Kullanıcı Maası : ", maas) #kullanıcı maası yazdırılır
print("Kullanıcı Öğrenci Mi : ", cevap) #kullanıcı öğrenci mi yazdırılır
print("Kullanıcı Adresi : ", adres) #kullanıcı adresi yazdırılır
print("--------------------------------")
x,y,z =10,20,30 # tek satırda x,y,z değerleri atanır
print("x =",x,"y =",y,"z =",z) #x,y,z değerleri yazdırılır
print(x+y+z) #x,y,z değerleri toplanır

ozet = f"""Kullanıcı Özeti\nAd Soyad: {ad_soyad}\nYaş: {yas}\nMaaş: {maas}\nÖğrenci mi: {cevap}\nAdres: {adres if adres is not None else '—'}\n"""
print(ozet)

dosya_adi = "log.txt"
with open(dosya_adi, "w", encoding="utf-8") as file:
    file.write(ozet)

print(f"Bilgiler {dosya_adi} dosyasına kaydedildi.")




