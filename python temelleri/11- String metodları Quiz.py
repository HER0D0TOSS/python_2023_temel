website =  "https://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

#1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk  karakterlerini silin.

x = ' Hello World '
yeni = x.strip()
print(yeni)


#2- 'https://www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin

a = website[12:22].strip()
result = website.strip('w.moc')
print(a)
print(result)

#3- 'course' karakter dizisindeki tüm karakterlerini küçük harf yapın.

b = course.lower()
print(b)

#4- 'website' içinde kaç tane a karakteri vardır?

sayac = website.count('a')
print(sayac)


#5- 'website' www ile başlayıp 'com' ile bitiyor mu?

print(website.startswith('www'))
print(website.endswith('com'))

#6- 'website' içinde '.com' ifadesi var mı?

print(".com" in website)


#7- 'course' içindeki karakterlerin hepsi alfabetik mi?

print(course.isalpha())

#8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.

contents = 'Contents'
cont = contents.center(50, '*')
print(cont)

#9- 'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.

bosluk = '-'.join(course)
print(bosluk)

#10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin.

metin = 'Hello World'

metin2 = metin.replace("World", "There")
print(metin2)


#11- 'course' karakter dizisini boşluk karakterlerinden ayırın.
