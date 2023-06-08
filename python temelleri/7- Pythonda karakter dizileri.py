name = 'Yavuzhan'
surname = 'OZGEN'
age = '23'

deneme = 'My name is '

print(deneme + name + surname) # BOYLE YAZILIRSA SONUC BİZE TÜM KARAKTERLERİN(DENEME HARİÇ) BİRLEŞİK ŞEKİLDE VERİR 'My name is YavuzhanOZGEN'

# BUNU ÖNLEMEK İÇİN YA BAŞLANGICTA STRING TANIMLANIRKEN ARASINA BOŞLUK YADA PRINT YAPARKEN ARALARA TIRNAK EKLENMELİDİR. ÖRNEK;

print(deneme + name + ' '+ surname) # BU İŞLEM YAPILDIGINDA ÇIKIŞ OLARAK 'My name is Yavuzhan OZGEN' YAZAR.

##################################################################################################################################

"""
 ŞİMDİ BÜTÜN DEĞİŞKENLERİ BİRLEŞTİRELİM
"""
print(deneme + name + ' ' + surname +' '+ 'I AM' + ' ' + age + ' ' + 'YEARS OLD') # ÇIKIŞ OLARAK 'My name is Yavuzhan OZGENI am 23 years old'


"""
    KAÇIŞ KARAKTERİ KULLANIMI(\n)
"""

print(deneme + name + ' ' + surname + ' AND\nI AM' + ' ' + age + ' ' + 'YEARS OLD') # BU ŞEKİLDE YAZILIRSA I AM KISMINDAN SONRAKİ KISIM ALT SATIRA YAZILIR.


"""
    INDEX MANTIGI

"""

greeting = 'MY NAME IS' + name + ' ' + surname + ' AND\nI AM' + ' ' + age + ' ' + 'YEARS OLD'

print(greeting[2]) # INDEXLEMEDE 0 MANTIGI HER BİR STRING VERİSİNİN İLK KARAKTERİ 0 İLE BAŞLAR 2. KARAKTER 1. İNDEX OLUR ORNEK;

# M -----> 0
# Y -----> 1
# '' ----> 2
# N -----> 3  BOYLE DEVAM EDER.

#### TERS ŞEKİLDE DE INDEX ALABİLİRİZ BU SEFER SON HARF VEYA SAYI VB. -1 OLUR VE SIRALAMA GERİYE DOGRU GİDER.

print(greeting[-2])

# D -----> -1
# L -----> -2
# O ----> -3
#'' -----> -4 BOYLE DEVAM EDER.

"""
    'len()' kullanımı
"""
# İÇİNE GİREN LİSTENİN ELEMAN SAYISINI VEYA UZUNLUGUNU VERİR

greeting = 'MY NAME IS' + name + ' ' + surname + ' AND\nI AM' + ' ' + age + ' ' + 'YEARS OLD'

listeUzunluğu = len(greeting)

print(listeUzunluğu)


"""
    INDEXLERE ARALIK VEREBİLİRİZ
"""

greeting = 'MY NAME IS' + name + ' ' + surname + ' AND\nI AM' + ' ' + age + ' ' + 'YEARS OLD'

print(greeting[2:5]) # 2. indexten başlar 5. index hariç 2, 3 ve 4. indexi ekrana yazar
print(greeting[3:]) # 3. indexten itibaren herşeyi ekrana yazar 
print(greeting[:16])# 0. indexten 16. indexe kadar her şeyi yazar
print(greeting[2:40:2]) #2. indexten 40. indexe kadar değerleri alır ancak alma koşulu 2 karakter atlayarak alır