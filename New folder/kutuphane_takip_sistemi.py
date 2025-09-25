import sys

kitaplar = []

# Yardımcı: kayıt içinden kitap adını string olarak al (str ya da tek elemanlı set olabilir)
def _kitap_adini_al(kayit):
    return next(iter(kayit)) if isinstance(kayit, set) and len(kayit) == 1 else kayit

# Yardımcı: aynı isimli kitap var mı? (büyük/küçük harfe duyarsız)
def ayni_kitap_var_mi(ad):
    aranan = str(ad).strip().casefold()
    return any(aranan == str(_kitap_adini_al(k)).strip().casefold() for k in kitaplar)
#Kitap Ekleme 
def kitap_ekle ():
    eklenecek_kitap = input("Eklenecek Kitabın ismini giriniz : ")
    if ayni_kitap_var_mi(eklenecek_kitap):
        print("Bu kitap zaten listede var.")
        with open ("kitap_takip.txt","a", encoding= "utf-8") as file :
         print(f" Aynı Kitap Ekleme Denemesi Engellendi : {eklenecek_kitap}",file)
        return
    # Kitapları string olarak sakla
    kitaplar.append(str(eklenecek_kitap))
    with open ("kitap_takip.txt","a", encoding= "utf-8") as file :
     print(f" Kitap Eklendi : {eklenecek_kitap}",file)    


#Kitap Silme
def kitap_sil():
    silinecek_kitap = input("Simek istenilen kitabı ismini Girinniz : ")
    hedef = str(silinecek_kitap).strip().casefold()
    indeks = next((i for i, k in enumerate(kitaplar)
                   if hedef == str(_kitap_adini_al(k)).strip().casefold()), None)
    if indeks is None:
        print("Silinecek kitap bulunamadı.")
        with open ("kitap_takip.txt","a", encoding= "utf-8") as file :
         print(f" Silme Denemesi: Bulunamadı -> {silinecek_kitap}",file)
        return
    silinen = kitaplar.pop(indeks)
    with open ("kitap_takip.txt","a", encoding= "utf-8") as file :
     print(f" Kitap Silindi : {silinen}",file)    

#Kitap listele
def kitap_listele ():
    for index , kitap in enumerate(kitaplar,1) :
        print(f"{index}. Kitap ismi : {_kitap_adini_al(kitap)}")
        with open ("kitap_takip.txt","a", encoding= "utf-8") as file :
         print(f" Kitaplar Listelendi : {_kitap_adini_al(kitap)}",file)    


  

#Kitap Ara
def kitap_ara ():
    aranan_kitap = input("Aramak istediginiz kitabın ismini giriniz : ")
    aranan = aranan_kitap.strip().casefold()
    bulunan_kitaplar = [
        _kitap_adini_al(kitap) for kitap in kitaplar
        if aranan and aranan in str(_kitap_adini_al(kitap)).casefold()
    ]
    if bulunan_kitaplar:
        print(f"Bulunan Kitaplar: {bulunan_kitaplar}")
    else:
        print("Kitap Bulunamadı")
    with open ("kitap_takip.txt","a", encoding= "utf-8") as file :
         print(f" Kitaplar Arandı : {bulunan_kitaplar}",file)    

   
def alfabetik_sırala ():
    kitaplar.sort(key=lambda k: str(_kitap_adini_al(k)).casefold())
    print(f" Kitaplar Alfabetik Sıralandı {kitaplar}")
    with open ("kitap_takip.txt","a", encoding= "utf-8") as file :
         print(f" Kitaplar Alfabetik Sıralandı {kitaplar}",file) 


def kitap_listesi_ters_cevir ():
    kitaplar.reverse()
    print (f" Kitaplar Listesi Ters Sıralandı {kitaplar}")
    with open ("kitap_takip.txt","a", encoding= "utf-8") as file :
         print(f" Kitaplar Listesi Ters Sıralandı {kitaplar}",file) 





def kitap_indexi_bul ():
    ad = input("Indexini bulmak istediğiniz kitap adı: ")
    hedef = str(ad).strip().casefold()
    indeks = next((i for i, k in enumerate(kitaplar)
                   if hedef == str(_kitap_adini_al(k)).strip().casefold()), None)
    if indeks is None:
        print("Kitap bulunamadı.")
    else:
        print(f"Kitap İndex No : {indeks}")
    with open ("kitap_takip.txt","a", encoding= "utf-8") as file :
         print(f" Kitap Index Arandı : {ad} -> {indeks}",file) 





def liste_kopyala():
    kopyalanan_liste = kitaplar.copy()
    print(f"Kopyalanan Liste : {kopyalanan_liste}")
    with open ("kitap_takip.txt","a", encoding= "utf-8") as file :
         print(f" Kopyalanan Liste : {kopyalanan_liste}",file) 



def listeyi_temizle ():
    kitaplar.clear()
    print(f"Liste Temizlendi : ")
    with open ("kitap_takip.txt","a", encoding= "utf-8") as file :
         print(f" Liste Temizlendi : ",file) 



def liste_bosMu_kontrolu ():
    if not kitaplar:
     print("Liste boş.")
    else:
     print("Listede eleman var.")




 
def aynı_kitap_kontrolu():
    ad = input("Kontrol etmek istediğiniz kitap adını giriniz: ")
    if ayni_kitap_var_mi(ad):
        print( f"Aynı isimli kitap zaten mevcut: {ad}")
    else:
       print(f"Bu isimde kayıt bulunamadı: {ad}")
    
    with open ("kitap_takip.txt","a", encoding= "utf-8") as file :
     print("Aynı Kitap Var Mı Kontrol Edildi", file=file)


def cıkıs ():
    print("Programdan çıkılıyor...")
    with open ("kitap_takip.txt","a", encoding= "utf-8") as file :
     print("Programdan çıkıldı", file=file)
    sys.exit(0)





while True :
    print("Kutuphana Takip Sistemi")
    print("1-  Kitap Ekle")
    print("2-  Kitap Sil")
    print("3-  Kitap Listele")
    print("4-  Kitap Ara")
    print("5-  Kitap Alfabetik Sırala")
    print("6-  Kitap Listesini Ters Cevir")
    print("7-  Kitap Indexini Bul")
    print("8-  Listeyi Kopyala")
    print("9-  Listeyi Temizle")
    print("10- Liste Bos Mu Kontrolu ")
    print("11- Aynı Kitap Kontrolu")
    print("12- Cıkıs")


    secim = input("Yapmak istediğiniz İslem No Seciniz: ").strip()
    if secim == "1":
        kitap_ekle()
    elif secim == "2":
        kitap_sil()
    elif secim == "3":
        kitap_listele()
    elif secim == "4":
        kitap_ara()
    elif secim == "5":
        alfabetik_sırala()
    elif secim == "6":
        kitap_listesi_ters_cevir()
    elif secim == "7":
        kitap_indexi_bul()
    elif secim == "8":
        liste_kopyala()
    elif secim == "9":
        listeyi_temizle()
    elif secim == "10":
        liste_bosMu_kontrolu()
    elif secim == "11":
        aynı_kitap_kontrolu()
    elif secim == "12":
        cıkıs()
    else :
        print("Gecersiz Deger Girdiniz")










