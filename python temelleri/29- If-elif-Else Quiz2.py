#1- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol eden python uygulamasını yapınız.

sayi = int(input("SAYI GİRİNİZ: "))

if(sayi>=0) and (sayi%2==0):
    print(f"GİRİLEN SAYI ÇİFTTİR BU SAYI: {sayi}")
else:
    print(f"GİRİLEN SAYI TEKTİR BU SAYI: {sayi}")



#2-  Email ve parola bilgileri ile giriş kontrolü yapınız.

sistem_eposta = "sistem@gmail.com"
sistem_sifre  = "sistem123"

kisi_eposta = input("LUTFEN E POSTANIZI GİRİNİZ: ")
kisi_sifre = input("LUTFEN SİFRENİZİ GİRİNİZ:")

if(sistem_eposta == kisi_eposta) and (sistem_sifre == kisi_sifre):
    print(f"BU KİŞİ SİSTEME KAYITLI")
else:
    print(f'BU KİŞİ SİSTEME KAYITLI DEĞİL')


#3- Girilen 3 sayıyı büyüklük olarak karşılaştıran python uygulamasını yapınız.

a = int(input("1. sayı değeri: "))
b = int(input("2. sayı değeri: "))
c = int(input("3. sayı değeri: "))

if(a>b) and (a>c):
    print(f"EN BÜYÜK SAYI {a}")

elif(b>a) and (b>c):
    print(f"EN BÜYÜK SAYI {b}")

else:
    print(f"EN BÜYÜK SAYI {c}")

#5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayan python uygulamasını yapınız.

#       Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#       a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
#       b-) Finalden 70 alındığında ortalamanın önemi olmasın.


vize_1 = int(input('BİRİNCİ VİZEYİ GİRİN: '))
vize_2 = int(input('İKİNCİ VİZEYİ GİRİN: '))
final = int(input("Final SONUCUNU GİRİN: "))

not_durumu = (((vize_1 + vize_2)*0.6) + (final * 0.4))

if(not_durumu >= 50):
    print("GEÇTİNİZ")

    if(final==50):
        print("GEÇTİNİZ")

        