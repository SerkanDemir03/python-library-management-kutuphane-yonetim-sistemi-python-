import json
import os


def json_oku(dosya_adi):
    """Verilen dosya varsa JSON içeriğini liste olarak döner, yoksa boş liste döner."""
    if os.path.exists(dosya_adi):
        with open(dosya_adi, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def json_yaz(dosya_adi, veri):
    """Verilen listeyi JSON dosyasına kaydeder."""
    with open(dosya_adi, 'w', encoding='utf-8') as f:
        json.dump(veri, f, indent=4)


kitaplar = json_oku("books.json")
kullanicilar = json_oku("users.json")


def kitap_ara(kitap_adi):
    """Girilen ada göre kitap arar ve bulursa ekrana yazar."""
    for kitap in kitaplar:
        if kitap_adi.lower() in kitap["kitap_ad"].lower():
            print(f"Kitap: {kitap['kitap_ad']} | Yazar: {kitap['yazar']} | Yıl: {kitap['yil']} | ISBN: {kitap['isbn']}")
            return
    print("Bu ada uygun kitap bulunamadı.")

def kitap_odunc_ver(kullanici_adi, kitap_adi):
    """Belirtilen kullanıcıya, varsa kitabı ödünç verir."""
    for kitap in kitaplar:
        if kitap_adi.lower() == kitap["kitap_ad"].lower():
            for kullanici in kullanicilar:
                if kullanici_adi.lower() == kullanici["ad"].lower():

                    # Kullanıcı zaten almış mı?
                    if kitap in kullanici["odunc_kitaplar"]:
                        print(f"{kullanici_adi} bu kitabı zaten ödünç almış.")
                    else:
                        kullanici["odunc_kitaplar"].append(kitap)
                        kitaplar.remove(kitap)
                        print(f"{kullanici_adi} '{kitap_adi}' kitabını ödünç aldı.")
                        # Değişiklikleri kaydet
                        json_yaz("books.json", kitaplar)
                        json_yaz("users.json", kullanicilar)
                    return
    print("Kitap ödünç verilemedi (kitap mevcut değil veya kullanıcı bulunamadı).")

def kitap_iade_et(kullanici_adi, kitap_adi):
    """Kullanıcının ödünç aldığı kitabı iade eder."""
    for kullanici in kullanicilar:
        if kullanici_adi.lower() == kullanici["ad"].lower():
            for kitap in kullanici["odunc_kitaplar"]:
                if kitap_adi.lower() == kitap["kitap_ad"].lower():
                    kullanici["odunc_kitaplar"].remove(kitap)
                    kitaplar.append(kitap)
                    print(f"{kullanici_adi} '{kitap_adi}' kitabını iade etti.")
                    # Değişiklikleri kaydet
                    json_yaz("books.json", kitaplar)
                    json_yaz("users.json", kullanicilar)
                    return
    print(f"{kullanici_adi} tarafından ödünç alınmış '{kitap_adi}' kitabı bulunamadı.")

def kullanici_kitaplarini_goster(kullanici_adi):
    """Bir kullanıcının ödünç aldığı tüm kitapları listeler."""
    for kullanici in kullanicilar:
        if kullanici_adi.lower() == kullanici["ad"].lower():
            if not kullanici["odunc_kitaplar"]:
                print(f"{kullanici_adi} tarafından ödünç alınan kitap yok.")
                return
            print(f"{kullanici_adi} tarafından ödünç alınan kitaplar:")
            for kitap in kullanici["odunc_kitaplar"]:
                print(f"- {kitap['kitap_ad']} ({kitap['yil']})")
            return
    print("Kullanıcı bulunamadı.")

def tum_kitaplari_listele():
    """Kütüphanede şu an bulunan tüm kitapları listeler."""
    if not kitaplar:
        print("Kütüphanede hiç kitap yok.")
        return
    print("\n--- Kütüphanedeki Kitaplar ---")
    for kitap in kitaplar:
        print(f"Kitap: {kitap['kitap_ad']} | Yazar: {kitap['yazar']} | Yıl: {kitap['yil']} | ISBN: {kitap['isbn']}")


def kitap_ekle(kitap_ad, yazar, yil, isbn):
    """Yeni kitap ekler. ISBN benzersiz olmalı. JSON'a kaydeder."""
    # ISBN benzersizlik kontrolü (hem rafta hem ödünçte olabilir)
    isbn_lower = str(isbn).strip().lower()
    for k in kitaplar:
        if str(k.get("isbn", "")).strip().lower() == isbn_lower:
            print("Bu ISBN ile kayıtlı bir kitap zaten var.")
            return
    for kullanici in kullanicilar:
        for k in kullanici.get("odunc_kitaplar", []):
            if str(k.get("isbn", "")).strip().lower() == isbn_lower:
                print("Bu ISBN şu anda bir kullanıcıda ödünçte. Farklı bir ISBN deneyin.")
                return

    try:
        yil_int = int(yil)
    except ValueError:
        print("Yıl sayısal olmalıdır.")
        return

    yeni_kitap = {
        "kitap_ad": kitap_ad.strip(),
        "yazar": yazar.strip(),
        "yil": yil_int,
        "isbn": str(isbn).strip()
    }
    kitaplar.append(yeni_kitap)
    json_yaz("books.json", kitaplar)
    print(f"'{kitap_ad}' eklendi.")


def kitap_sil(anahtar):
    """ISBN veya kitap adına göre raftaki kitabı siler. Ödünçteyse silmez."""
    key = str(anahtar).strip().lower()

    # Önce ödünçte mi kontrol et (isbn veya ad ile)
    for kullanici in kullanicilar:
        for k in kullanici.get("odunc_kitaplar", []):
            if key == str(k.get("isbn", "")).strip().lower() or \
               key == str(k.get("kitap_ad", "")).strip().lower():
                print("Bu kitap şu anda ödünçte. İade edilmeden silinemez.")
                return

    # Raftan sil
    for k in list(kitaplar):
        if key == str(k.get("isbn", "")).strip().lower() or \
           key == str(k.get("kitap_ad", "")).strip().lower():
            kitaplar.remove(k)
            json_yaz("books.json", kitaplar)
            print(f"'{k['kitap_ad']}' silindi.")
            return

    print("Silinecek kitap bulunamadı.")


def kullanici_ekle(ad):
    """Yeni kullanıcı ekler. İsim benzersiz, id otomatik artar. JSON'a kaydeder."""
    ad_temiz = str(ad).strip()
    if not ad_temiz:
        print("Kullanıcı adı boş olamaz.")
        return

    # İsim benzersizliği (case-insensitive)
    for u in kullanicilar:
        if ad_temiz.lower() == str(u.get("ad", "")).strip().lower():
            print("Bu isimde bir kullanıcı zaten var.")
            return

    yeni_id = (max([u.get("id", 0) for u in kullanicilar]) + 1) if kullanicilar else 1
    yeni_kullanici = {"ad": ad_temiz, "id": yeni_id, "odunc_kitaplar": []}
    kullanicilar.append(yeni_kullanici)
    json_yaz("users.json", kullanicilar)
    print(f"Kullanıcı eklendi: {ad_temiz} (id={yeni_id})")


def kullanici_sil(anahtar):
    """İsim veya id ile kullanıcı siler. Ödünç kitabı varsa silmez."""
    key = str(anahtar).strip().lower()

    for u in list(kullanicilar):
        isim_eslesme = key == str(u.get("ad", "")).strip().lower()
        id_eslesme = key.isdigit() and int(key) == u.get("id")
        if isim_eslesme or id_eslesme:
            if u.get("odunc_kitaplar"):
                print("Kullanıcının iade etmediği kitaplar var. Silinemez.")
                return
            kullanicilar.remove(u)
            json_yaz("users.json", kullanicilar)
            print("Kullanıcı silindi.")
            return

    print("Silinecek kullanıcı bulunamadı.")


def ana_menu():
    """Kullanıcıya sürekli menü gösterir ve seçimlere göre işlemleri çalıştırır."""
    while True:
        print("\n=== KÜTÜPHANE YÖNETİM SİSTEMİ ===")
        print("1) Kitap Ara")
        print("2) Kitap Ödünç Al")
        print("3) Kitap İade Et")
        print("4) Kullanıcının Ödünç Aldığı Kitaplar")
        print("5) Kütüphanedeki Tüm Kitaplar")
        print("6) Kitap Ekle")
        print("7) Kitap Sil")
        print("8) Kullanıcı Ekle")
        print("9) Kullanıcı Sil")
        print("10) Çıkış")

        secim = input("Seçiminiz (1-10): ").strip()

        if secim == "1":
            kitap_ara(input("Kitap adı: "))
        elif secim == "2":
            kitap_odunc_ver(input("Kullanıcı adı: "), input("Kitap adı: "))
        elif secim == "3":
            kitap_iade_et(input("Kullanıcı adı: "), input("Kitap adı: "))
        elif secim == "4":
            kullanici_kitaplarini_goster(input("Kullanıcı adı: "))
        elif secim == "5":
            tum_kitaplari_listele()
        elif secim == "6":
            kitap_ekle(
                input("Kitap adı: "),
                input("Yazar: "),
                input("Yıl: "),
                input("ISBN: ")
            )
        elif secim == "7":
            kitap_sil(input("Silinecek kitap adı veya ISBN: "))
        elif secim == "8":
            kullanici_ekle(input("Kullanıcı adı: "))
        elif secim == "9":
            kullanici_sil(input("Silinecek kullanıcı adı veya ID: "))
        elif secim == "10":
            print("Program sonlandırılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen 1-10 arası bir sayı girin.")


ana_menu()
