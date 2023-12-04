kitaplar = {}

def kitap_ekle(baslik, yazar, yayinevi, fiyat, kategori):
    kitap = {"baslik": baslik, "yazar": yazar, "yayinevi": yayinevi, "fiyat": fiyat, "kategori": kategori}
    if baslik in kitaplar:
        kitaplar[baslik]["sayi"] += 1
    else:
        kitaplar[baslik] = kitap
        kitaplar[baslik]["sayi"] = 1

def indirim_uygula(kitaplar):
    toplam_fiyat = sum(kitap["fiyat"] * kitap["sayi"] for kitap in kitaplar.values())
    indirim_miktari = 0
    indirimli_kitaplar = []

    for baslik, kitap in kitaplar.items():
        if kitap["sayi"] >= 3:
            indirim_miktari += kitap["fiyat"]
            indirimli_kitaplar.append(kitap)

    if len(kitaplar) >= 4:
        en_ucuz_kitap = min(kitaplar.values(), key=lambda x: x["fiyat"])
        indirim_miktari += en_ucuz_kitap["fiyat"]
        indirimli_kitaplar.append(en_ucuz_kitap)

    yayinevleri = set(kitap["yayinevi"] for kitap in kitaplar.values())
    if len(kitaplar) >= 2 and len(yayinevleri) == 1:
        indirim_miktari += toplam_fiyat * 0.05

    if len(kitaplar) >= 3 and len(yayinevleri) == 1:
        indirim_miktari += toplam_fiyat * 0.07

    yazarlar = {}
    for kitap in kitaplar.values():
        if kitap["yazar"] in yazarlar:
            yazarlar[kitap["yazar"]]["sayi"] += 1
        else:
            yazarlar[kitap["yazar"]] = {"sayi": 1, "en_ucuz_fiyat": kitap["fiyat"]}

    for yazar, bilgi in yazarlar.items():
        if bilgi["sayi"] >= 2:
            indirim_miktari += bilgi["en_ucuz_fiyat"] * 0.3
            indirimli_kitaplar.append(kitaplar[baslik])

    return indirim_miktari, indirimli_kitaplar

# Kullanım örneği
kitap_ekle("Dune", "Frank Herbert", "Remzi Kitabevi", 50, "Bilim Kurgu")
kitap_ekle("1984", "George Orwell", "Remzi Kitabevi", 40, "Distopya")
kitap_ekle("Bülbülü Öldürmek", "Harper Lee", "Remzi Kitabevi", 30, "Roman")
kitap_ekle("Büyük Gatsby", "F. Scott Fitzgerald", "Yapı Kredi Yayınları", 60, "Roman")
kitap_ekle("Moby Dick", "Herman Melville", "Yapı Kredi Yayınları", 70, "Roman")
kitap_ekle("Çavdar Tarlasında Çocuklar", "J.D. Salinger", "Yapı Kredi Yayınları", 80, "Roman")
kitap_ekle("Savaş ve Barış", "Leo Tolstoy", "Can Yayınları", 10, "Roman")
kitap_ekle("Gurur ve Önyargı", "Jane Austen", "Can Yayınları", 30, "Roman")
kitap_ekle("Suç ve Ceza", "Fyodor Dostoyevski", "Can Yayınları", 40, "Roman")
kitap_ekle("Cesur Yeni Dünya", "Aldous Huxley", "Can Yayınları", 50, "Distopya")

indirim_miktari, indirimli_kitaplar = indirim_uygula(kitaplar)
print("Alınan Kitaplar:")
for baslik, kitap in kitaplar.items():
    print(f"{kitap['baslik']} - {kitap['yazar']} - {kitap['yayinevi']} - {kitap['fiyat']} TL - Adet: {kitap['sayi']}")

print("\nİşlem Bilgisi:")
toplam_fiyat = sum(kitap["fiyat"] * kitap["sayi"] for kitap in kitaplar.values())
print(f"Toplam Tutar: {toplam_fiyat} TL")

if indirim_miktari > 0:
    print(f"İndirim Miktarı: {indirim_miktari} TL")
    print(f"İndirimli Tutar: {toplam_fiyat - indirim_miktari} TL")

    print("\nİndirim Uygulanan Kitaplar:")
    for kitap in indirimli_kitaplar:
        print(f"{kitap['baslik']} - {kitap['yazar']} - {kitap['yayinevi']} - {kitap['fiyat']} TL")
else:
    print("İndirim Uygulanmadı.")
