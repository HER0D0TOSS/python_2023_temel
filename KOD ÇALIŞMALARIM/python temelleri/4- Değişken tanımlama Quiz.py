"""
    1- BİR MÜŞTERİNİN AŞAĞIDAKİ BİLGİLERİ İÇİN DEĞİŞKEN OLUŞTURUNUZ.

    Müşteri Adı
    Müşsteri Soyadı
    Müşteri ad + soyad
    Müşteri cinsiyet
    Müşteri tc kimlik
    Müşteri dogum yili
    Müşteri adres bilgisi
    Müşteri yaşı
"""

"""
    2- AŞAĞIDAKİ SİPARİŞLERİN TOPLAM BİLGİSİNİ HESAPLAYINIZ

    Siparis 1 => 110 TL
    Siparis 2 => 1100.5 TL
    Siparis 3 => 356.95 TL
"""




# ÖRNEK 1

musteriAdi = "ali"
musteriSoyadi = "cezmi"
musteriAd_Soyad = musteriAdi + musteriSoyadi
musteriCinsiyet = "erkek"
musteriTc = 12312434213
musteriDogumyili = 1998
musteriAdres = "................"
musteriYasi = 23

print(f'MUSTERİ BİLGİLERİ: MUSTERİ ADI: {musteriAd_Soyad}, MUSTERİ CİNSİYET: {musteriCinsiyet}, MUSTERİ TC: {musteriTc}, MUSTERİ DOGUM YILI: {musteriDogumyili}, MUSTERİ ADRES: {musteriAdres}')


# ÖRNEK 2

siparis_1 = 110
siparis_2 = 1100.5
siparis_3 = 356.95

total = siparis_1 + siparis_2 + siparis_3

print(f'SİPARİŞLERİN TOPLAMI : {total} TL')
