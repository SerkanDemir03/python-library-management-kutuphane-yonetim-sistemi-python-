import json
import os

# JSON dosyalarını okuma ve yazma fonksiyonları
def dosyadan_okuma(dosya_adi):
    if os.path.exists(dosya_adi):
        with open(dosya_adi, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def dosyaya_yazma(dosya_adi, veri):
    with open(dosya_adi, 'w', encoding='utf-8') as f:
        json.dump(veri, f, indent=4)

# Kitaplar ve Kullanıcılar JSON dosyasından okunuyor
kitaplar = dosyadan_okuma("books.json")
kullanicilar = dosyadan_okuma("users.json")

# Kitap arama fonksiyonu
def kitap_arama(kitap_ad):
    for kitap in kitaplar:
        if kitap_ad.lower() in kitap["kitap_ad"].lower():
            print(f"Kitap Adı: {kitap['kitap_ad']}, Yazar: {kitap['yazar']}, Yıl: {kitap['yil']}, ISBN: {kitap['isbn']}")
            return
    print("Kitap bulunamadı.")

# Kitap ödünç alma fonksiyonu
def kitap_odunc_al(ad, kitap_ad):
    for kitap in kitaplar:
        if kitap_ad.lower() == kitap["kitap_ad"].lower():
            for kullanici in kullanicilar:
                if ad.lower() == kullanici["ad"].lower():
                    if kitap in kullanici["odunc_kitaplar"]:
                        print(f"{ad} bu kitabı zaten ödünç almış.")
                    else:
                        kullanici["odunc_kitaplar"].append(kitap)
                        kitaplar.remove(kitap)
                        print(f"{ad} başarılı bir şekilde {kitap_ad} kitabını ödünç aldı.")
                        # Veriyi dosyaya kaydet
                        dosyaya_yazma("books.json", kitaplar)
                        dosyaya_yazma("users.json", kullanicilar)
                    return
    print("Kitap ödünç alınamadı. Kitap mevcut olmayabilir.")

# Kitap iade etme fonksiyonu
def kitap_iade_et(ad, kitap_ad):
    for kullanici in kullanicilar:
        if ad.lower() == kullanici["ad"].lower():
            for kitap in kullanici["odunc_kitaplar"]:
                if kitap_ad.lower() == kitap["kitap_ad"].lower():
                    kullanici["odunc_kitaplar"].remove(kitap)
                    kitaplar.append(kitap)
                    print(f"{ad} {kitap_ad} kitabını iade etti.")
                    # Veriyi dosyaya kaydet
                    dosyaya_yazma("books.json", kitaplar)
                    dosyaya_yazma("users.json", kullanicilar)
                    return
    print(f"{ad} tarafından ödünç alınan {kitap_ad} kitabı bulunamadı.")

# Kullanıcıya göre ödünç alınan kitaplar
def kullanici_odunc_kitaplari(ad):
    for kullanici in kullanicilar:
        if ad.lower() == kullanici["ad"].lower():
            if not kullanici["odunc_kitaplar"]:
                print(f"{ad} tarafından ödünç alınan hiç kitap yok.")
                return
            print(f"{ad} tarafından ödünç alınan kitaplar: ")
            for kitap in kullanici["odunc_kitaplar"]:
                print(f"- {kitap['kitap_ad']} ({kitap['yil']})")
            return
    print("Kullanıcı bulunamadı.")

# Kitaplar listesini yazdırma
def kitaplar_listesini_yazdir():
    if kitaplar:
        print("\nKitaplar Listesi:")
        for kitap in kitaplar:
            print(f"Kitap Adı: {kitap['kitap_ad']}, Yazar: {kitap['yazar']}, Yıl: {kitap['yil']}, ISBN: {kitap['isbn']}")
    else:
        print("Kütüphanede kitap bulunmamaktadır.")

# Ana menü
def ana_menu():
    while True:
        print("\n--- Online Kütüphane Yönetim Sistemi ---")
        print("1. Kitap Arama")
        print("2. Kitap Ödünç Alma")
        print("3. Kitap İade Etme")
        print("4. Kullanıcıya Göre Ödünç Kitaplar")
        print("5. Kitaplar Listesini Görüntüle")
        print("6. Çıkış")

        secim = input("Bir seçenek girin (1-6): ")

        if secim == "1":
            kitap_ad = input("Aramak istediğiniz kitabın adını girin: ")
            kitap_arama(kitap_ad)

        elif secim == "2":
            ad = input("Kitap ödünç almak isteyen kullanıcı adı: ")
            kitap_ad = input("Ödünç almak istediğiniz kitabın adını girin: ")
            kitap_odunc_al(ad, kitap_ad)

        elif secim == "3":
            ad = input("Kitap iade etmek isteyen kullanıcı adı: ")
            kitap_ad = input("İade etmek istediğiniz kitabın adını girin: ")
            kitap_iade_et(ad, kitap_ad)

        elif secim == "4":
            ad = input("Ödünç aldığı kitapları görmek isteyen kullanıcı adı: ")
            kullanici_odunc_kitaplari(ad)

        elif secim == "5":
            kitaplar_listesini_yazdir()

        elif secim == "6":
            print("Çıkılıyor...")
            break
        
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

# Sistemi başlat
ana_menu()
