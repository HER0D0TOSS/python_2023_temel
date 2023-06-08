names = ['Ali', 'Yağmur', 'Hakan', 'Deniz']
years = [1998, 2000, 1998, 1987]

#1- "Cenk" ismini listenin sonuna ekleyiniz.

names.append("Cenk")
print(names)

#2- "Sena" değerini listenin başına ekleyiniz.

names.insert(0, "Sena")
print(names)

#3- "Deniz" ismini listeden siliniz.

names.remove("Deniz")
print(names)

#4- "Deniz" isminin indeksi nedir?

print(names.index("Deniz"))

#5- "Ali" listenin bir elemanı mıdır?

print("Ali" in names)

#6- Liste elemanlarını ters çeviriniz.

name = names.reverse()
print(names)

#7- Liste elemanlarını alfabetik olarak sıralayınız.

names2 = names.sort()
print(names)

#8- years listesini rakamsal büyüklüğüne göre sıralayınız.

years2 = years.sort()
print(years)

#9- str = "Chevrolet Dacia" karakter dizisini listeye çeviriniz.

str = "Chevrolet Dacia"
print(type(str))
str = str.split()
print(str)

#10- years dizisinin en büyük ve en küçük elemanı nedir?

sıra = years.sort()
min = years[0]
max = years[-1]
print(f"Listenin en küçük elemanı {min}, en büyük elemanı {max}")

#11- years dizisinde kaç tane 1998 değeri vardır?

print(years.count(1998))

#12- years dizisinin tüm elemanlarını siliniz.

print(f'ilk durum {len(years)}')
years.clear()
print(f'son durum {len(years)}')

#13- kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.

marka1 = input("1. MARKA: ")
marka2 = input("2. Marka: ")
marka3 = input("3. Marka: ")

markalarım = []

markalarım.append(marka1)
markalarım.append(marka2)
markalarım.append(marka3)

print(markalarım)
