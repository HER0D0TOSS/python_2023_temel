website = "https://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır ?

karakter_sayisi = len(course)
print(f' karakter sayisi: {karakter_sayisi} Karakaterdir'),

# 2- 'website' içinden www karakterlerini alın. 

where = website.find('w')
print(website[where: where+3])

print(website[8:11])


# 3- 'website' içinden com karakterlerini alın.
where = website.find('c')
print(website[where: where+3])

print(website[23:])
print(website[23:27])
print(website[-1:-4])
print(website[-3:])


# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın

print(course[:15])
print(course[-15:])


# 5- 'course' ifadesindeki karakterleri tersten yazdırın.
print(course[::-1])
##########################################################################################################

name, surname, age, job = 'Bora', 'Yılmaz', 32, 'mühendis'


# 6- Yukarıda verilen  değişkenler ile ekrana aşağıdaki ifadeyi yazdırın
#  'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis.'

print('Benim adım' +' '+ name +' '+ surname +' '+ "," +" "+ "Yaşım" + ' ' + str(age) +' '+ 've mesleğim' + ' '+ job)
print("Benim adım {} {}, Yaşım {} ve Mesleğim {}".format(name,surname,age,job))
print(f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}")


# 7- 'Hello world' ifadesindeki w harfini  'W' ile değiştirin

a = 'Hello world'

a = a[0:6] + 'W'+ a[-4:]

print(a)


#8- 'abc' ifadesini yan yana 3 defa yazdırın
karakter= "abc"

karakterlerim =3 * karakter
print(karakterlerim)