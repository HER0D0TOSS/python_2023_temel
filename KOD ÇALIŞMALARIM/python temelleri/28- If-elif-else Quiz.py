#1- KULLANICIDAN İSİM, YAŞ VE EĞİTİM BİLGİLERİNİ İSTEYİP EHLİYET ALABİLME DURUMUNU KONTROL EDİNİZ. EHLİYET ALMA KOŞULU EN AZ 18 VE
#   EĞİTİM DURUMU LİSE YA DA ÜNİVERSİTE OLMALIDIR.

kullaniciAdi = input("İSMİNİZİ GİRİN: ")
kullaniciYas = int(input("YAŞINIZI GİRİNİZ: "))
eğitimBilgisi = input("EĞİTİM DURUMUNUZU GİRİNİZ: ")

ehliyetYas = 18
ehliyet_Eğitim = ['lise', 'üniversite']

if(kullaniciYas >= ehliyetYas) and (eğitimBilgisi in ehliyet_Eğitim):
    print(f'{kullaniciAdi} EHLİYET ALABİLİR')
else:
    print(f'{kullaniciAdi} EHLİYET ALAMAZ')


#2- BİR ÖĞRENCİNİN 2 YAZILI BİR SÖZLÜ NOTUNU ALIP HESAPLANAN ORTALAMAYA GÖRE NOT ARALIĞINA KARŞILIK GELEN NOT  BİLGİSİNİ YAZDIRINIZ.
#         0-24 => 0
#        25-44 => 1
#        45-54 => 2
#        55-69 => 3
#        70-84 => 4
#       85-100 => 5

yazılı_1 = int(input("1. SINAV SONUCUNU GİRİNİZ: "))
yazılı_2 = int(input("2. SINAV SONUCUNU GİRİNİZ: "))
sözlü    = int(input("SÖZLÜ NOTUNU GİRİNİZ: "))

not_hesabı = ((yazılı_1 + yazılı_2) / 2) + sözlü 

if(not_hesabı >=0 and not_hesabı<= 24):
    print(f"NOTUNUZ {not_hesabı}, DURUM: 0")

elif(not_hesabı >=25 and not_hesabı<= 44):
    print(f"NOTUNUZ {not_hesabı}, DURUM: 1")

elif(not_hesabı >=45 and not_hesabı<= 54):
    print(f"NOTUNUZ {not_hesabı}, DURUM: 2")

elif(not_hesabı >=55 and not_hesabı<= 69):
    print(f"NOTUNUZ {not_hesabı}, DURUM: 3")

elif(not_hesabı >=70 and not_hesabı<= 84):
    print(f"NOTUNUZ {not_hesabı}, DURUM: 4")

elif(not_hesabı >=85 and not_hesabı<= 100):
    print(f"NOTUNUZ {not_hesabı}, DURUM: 5")

#3- TRAFİĞE ÇIKIŞ TARİHİ ALINAN BİR ARACIN SERVİS ZAMANINI AŞAĞIDAKİ BİLGİLERE GÖRE HESAPLAYINIZ.
#       1. Bakım => 1. yıl
#       2. Bakım => 2. yıl
#       3. Bakım => 3. yıl
#
#       ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız.
#       *** datetime modülünü kullanmanız gerekiyor


import datetime

tarih = input('aracınız hangi tarihte trafiğe çıktı (2019/8/9): ')
tarih = tarih.split('/')
trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))

simdi = datetime.datetime.now()
fark = simdi - trafigeCikis
days = fark.days

if days<=365:
     print('1.servis aralığı')
elif days>365 and days<=365*2:
     print('2.servis aralığı')
elif days>365*2 and days<=365*3:
    print('3.servis aralığı')
else:
    print('hatalı süre.')
