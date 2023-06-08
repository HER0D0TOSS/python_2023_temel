#1- GİRİLEN BİR SAYININ 0-100 ARASINDA OLUP OLMADIĞINI KONTROL EDİNİZ.

sayi = int(input("SAYI DEGERİNİ GİRİNİZ: "))

durum = (sayi>=0 and sayi<=100)
print(f'SAYİ İSTENEN ARALIKTA MI?: {durum}')

#2- GİRİLEN BİR SAYININ POZİTİF ÇİFT SAYI OLUP OLMADIĞINI KONTROL EDİNİZ.

sayi2 = int(input("SAYI DEGERİNİ GİRİNİZ: "))

sayidurum = (sayi2%2)
sonuc = (sayidurum == 0) and (sayi2 >=0)

print(f'girilen sayı pozitif bir çift sayıdır: {sonuc}')

#3- EMAİL VE PAROLA BİLGİLERİ İLE GİRİŞ KONTROLÜ YAPINIZ.

sistemEposta = 'www123@gmail.com'
sistempsswd = '123a'

kisiEposta = input("LÜTFEN SİSTEME KAYITLI ELEKTRONİK POSTA ADRESİNİZİ GİRİNİZ: ")
kisiPasswd = input("LÜTFEN SİSTEME KAYITLI ŞİFRENİZİ GİRİNİZ: ")

kayıt = (sistemEposta == kisiEposta) and (sistempsswd == kisiPasswd)
print(f'SİSTEME GİRİS BASARILI {kayıt}')


#4- GİRİLEN 3 SAYIYI BÜYÜKLÜK OLARAK KARŞILAŞTIRINIZ.

a = int(input("SAYI 1: "))
b = int(input("SAYI 2: "))
c = int(input("SAYI 3: "))

x = (a>b) and (a>c)
print(f'EN BÜYÜK SAYISAL DEGER a DIR: {x}')

y = (b>a) and (b>c)
print(f'EN BÜYÜK SAYISAL DEGER b DIR: {y}')

z = (c>a) and (c>b)
print(f'EN BÜYÜK SAYISAL DEGER c DIR: {z}')


#5- KULLANICIDAN 2 VİZE(%60) VE FİNAL (%40) NOTUNU ALIP ORTALAMA HESAPLAYINIZ.
#      EĞER ORTALAMA 50 VE ÜSTÜNDEYSE GEÇTİ DEĞİLSE KALDI YAZDIRIN.
#      a-) ORTALAMA 50 OLSA BİLE FİNAL NOTU EN AZ 50 OLMALIDIR.
#      b-) FİNALDEN 70 ALINDIĞINDA ORTALAMANIN ÖNEMİ OLMASIN

vize_1 = int(input("1. VİZE SONUCUNU GİRİNİZ: "))
vize_2 = int(input("2. VİZE SONUCUNU GİRİNİZ: "))
final  = int(input("FİNAL SONUCUNU GİRİNİZ: "))

sonuc_ort = (((vize_1 + vize_2)/2)*0.6) + (final * 0.4)

ortalama = sonuc_ort >= 50
print(f"SINAV NOT ORTALAMASI: {sonuc_ort}, GECME DURUMU: {ortalama}")

sonuc_ort2 = sonuc_ort >= 50 and final >=50
print(f"SINAV NOT ORTALAMASI: {sonuc_ort}, GECME DURUMU: {sonuc_ort2}")

sonuc_ort3 = sonuc_ort >= 50 or final >=70
print(f"SINAV NOT ORTALAMASI: {sonuc_ort}, GECME DURUMU: {sonuc_ort3}")


#6- KİŞİNİN AD, KİLO VE BOY BİLGİLERİNİ ALIP KİLO İNDEKSLERİNİ HESAPLAYINIZ.
#   FORMÜL (KİLO / BOY UZUNLUGU KARESİ)
#   AŞAĞIDAKİ TABLOYA GÖRE KİŞİ HANGİ GRUBA GİRMEKTEDİR.
#   0-18.4    => ZAYIF
#   18.5-24.9 => NORMAL
#   25.0-29.9 => FAZLA KİLOLU
#   30.0-34.9 => ŞİŞMAN (OBEZ)

ad = input("İSMİNİZİ GİRİNİZ: ")
kilo = int(input("KİLONUZU GİRİNİZ: "))
boy = int(input("BOYUNUZU GİRİNİZ: "))

indeks = (kilo / (boy**2))

durum_1 = ((indeks>=0) and (indeks<=18.4))
durum_2 = ((indeks>=18.5) and (indeks<=24.9))
durum_3 = ((indeks>=25.9) and (indeks<=29.9))
durum_4 = ((indeks>=30.0) and (indeks<=34.9))

print(f"KİLONUZ: : {indeks}, ZAYIF: {durum_1}")
print(f"KİLONUZ: : {indeks}, NORMAL: {durum_2}")
print(f"KİLONUZ: : {indeks}, FAZLA KİLOLU: {durum_3}")
print(f"KİLONUZ: : {indeks}, ŞİŞMAN(OBEZ): {durum_4}")
