
#1- GİRİLEN 2 SAYIDAN HANGİSİ BÜYÜKTÜR?

a = int(input("sayi 1: "))
b = int(input("sayi 2: "))

print(a>b)
print(b>a)

#2- KULLANICIDAN 2 VİZE(%60) VE FİNAL(%40) NOTUNU ALIP ORTALAMASINI HESAPLAYINIZ.
#   EĞER ORTALAMA 50 VE ÜZERİNDEYSE GEÇTİ DEİLSE KALDI YAZDIRIN.

vize_1 = int(input("vize 1: "))
vize_2 = int(input("vize 2: "))
final = int(input("fial : "))

vizeNot = (vize_1 + vize_2)* 60/100
finalNot = final * 40/100

toplam = vizeNot + final 
print(toplam)



#3- GİRİLEN BİR SAYININ TEK Mİ ÇİFT Mİ OLDUGUNU YAZDIRIN.

sayi = int(input("SAYİ DEGERİ GİRİNİZ: "))

durum = sayi % 2
print(f'girilen deger çift mi?: {durum==0}')
print(f'girilen değer tek mi?:  {durum > 0}')


#4- GİRİLEN BİR SAYININ NEGATİF POZİTİF DURUMUNU YAZDIRIN.

sayim = int(input("sayiyi girin: "))

pozitif_mi = sayim >= 0
negatif_mi = sayim < 0

print(f'Girilen değer pozitif mi?: {pozitif_mi}')
print(f'Girilen değer negatif mi?: {negatif_mi}')

#5- PAROLA VE EMAIL BİLGİSİNİ İSTEYİP DOĞRULUĞUNU KONTROL EDİNİZ.
#   (email: email@sadikturan.com parola: abc123)


sistemEmail = 'email@sadikturan.com'
sistemPsswd = 'abc123'

eposta = input("LÜTFEN ELEKTRONİK POSTA ADRESİNİZİ GİRİNİZ: ")
sifre = input("LÜTFEN SİSTEME KAYITLI ŞİFRENİZİ GİRİNİZ: ")

print(f'sistem e postası dogru mu?: {sistemEmail == eposta}')
print(f'sistem sifresi dogru mu?:   {sistemPsswd == sifre}')