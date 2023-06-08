#1- "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz. 

arabalar = ["Bmw", "Mercedes", "Opel", "Mazda"]
print(arabalar)
print(type(arabalar))

#2- Liste kaç elemanlıdır?

listeUzunluk = len(arabalar)
print(listeUzunluk)

#3- Listenin ilk ve son elemanı nedir?

ilkEleman = arabalar[0]
sonEleman = arabalar[3]
print(f'Listenin ilk elemanı: {ilkEleman}, son elemanı: {sonEleman}')

#4- Mazda değerini Toyota ile değiştirin.

arabalar[3] = "Toyota"
print(arabalar)

#5- Mercedes listenin bir elemanı mıdır?

print("Mercedes" in arabalar)

#6- Listenin -2 indeksindeki değer nedir?

print(arabalar[-2])

#7- Listenin ilk 3 elemanını alın.

print(arabalar[:3])

#8- Listenin son 2 elemanı yerine "Toyota" ve "Reanult" değerlerini ekleyin.

arabalar[-2:] = "Toyota", "Reanault"
print(arabalar)

#9- Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.

arabalar.append("Audi")
arabalar.append("Nissan")
print(arabalar)

#10- Listenin son elemanını silin

print(arabalar)
arabalar.pop(-1)
print(arabalar)

#11- Liste elemanlarını tersten yazdırınız.

print(arabalar[::-1])
print(list(reversed(arabalar)))

#12- Aşağıdaki verileri bir liste içinde saklayınız.

    # studentA: Yiğit Bilgi 2010, (70, 60, 70)
    # studentB: Sena Turan  1999, (80, 80, 70)
    # studentC: Ahmet Turan 1998, (80, 70, 90)


studentA = ["Yiğit", "Bilgi", 2010, [70, 60, 70]]
studentB = ["Sena", "Turan",  1999, [80, 80, 70]]
studentC = ["Ahmet", "Turan", 1998, [80, 70, 90]]


#13- Liste elemanlarını ekrana yazdırınız.

print(studentA[0])
print(studentB[1][0])
print(studentC[3][2])

print(f'{studentA[0]} {studentA[1]} {2023-2010} YAŞINDA VE NOT ORTALAMASI {(70+70+60)/2}')