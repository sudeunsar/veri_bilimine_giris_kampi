import statistics
import random
kitaplar = [
{"isim": "Veri Bilimi 101", "yazar": "Ali", "tur": "Bilim", "satis": 1200, "yil": 2021},
{"isim": "Python ile Yapay Zeka", "yazar": "Ayşe", "tur": "Bilim", "satis": 950, "yil": 2020},
{"isim": "İstatistik Temelleri", "yazar": "Ali", "tur": "Akademik", "satis": 700, "yil": 2019},
{"isim": "Makine Öğrenmesi", "yazar": "Can", "tur": "Bilim", "satis": 1800, "yil": 2022},
{"isim": "Veri Görselleştirme", "yazar": "Deniz", "tur": "Sanat", "satis": 400, "yil": 2018},
{"isim": "Matematiksel Modelleme", "yazar": "Ali", "tur": "Akademik", "satis": 1500, "yil": 2021},
{"isim": "Bilgi Toplumu", "yazar": "Ayşe", "tur": "Sosyal", "satis": 600, "yil": 2022}
 ]

#1
def en_cok_satan(kitaplar):
    return max(kitaplar, key=lambda k: k["satis"])
def yazar_satislari(kitaplar):
    toplam_satis = {}
    for kitap in kitaplar:
        yazar = kitap["yazar"]
        satis = kitap["satis"]
        if yazar in toplam_satis:
            toplam_satis[yazar] += satis
        else:
            toplam_satis[yazar] = satis
    return toplam_satis
print("En çok satan kitap:", en_cok_satan(kitaplar))
print("Yazar satışları:", yazar_satislari(kitaplar))

#2
for kitap in kitaplar:
    turler = kitap["tur"]
    print("Tum kitap turleri: " , turler)

    if kitap["satis"] > 1000:
        cok_satan_kitaplar = kitap["isim"]
        print("Satis adedi 1000'den fazla olan kitaplar: " , cok_satan_kitaplar)

#3
kitaplar_2020_sonrasi = list(filter(lambda k: k["yil"] > 2020, kitaplar))
print("2020’den sonra cikan kitaplar:", kitaplar_2020_sonrasi)

artirilmis_satis = list(map(lambda k: k["satis"] * 1.10, kitaplar))
print("Satislar %10 artirilmis:", artirilmis_satis)

siralanmis = sorted(kitaplar, key=lambda k: k["satis"], reverse=True)
print("Satis miktarina gore azalan siralama:", siralanmis)

#4
satislar = [k["satis"] for k in kitaplar]
ortalama_satis = statistics.mean(satislar)
print("Ortalama satis adedi :", ortalama_satis)

tur_satis = {}
for k in kitaplar:
    tur = k["tur"]
    if tur in tur_satis:
        tur_satis[tur] += k["satis"]
    else:
        tur_satis[tur] = k["satis"]

en_cok_satan_tur = max(tur_satis, key=tur_satis.get)
print("En cok satis yapan tur:", en_cok_satan_tur)

std_sap = statistics.stdev(satislar)
print("Satislerin standart sapmasi :", std_sap)

#5'i yapamadim