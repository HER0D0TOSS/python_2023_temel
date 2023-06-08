x, y, z = 2, 5, 10


numbers = 1, 5, 7, 10, 6


#1- KULLANICIDAN ALDIĞINIZ 2 SAYININ ÇARPIMI İLE x, y, z TOPLAMININ FARKI NEDİR?

sayi_1 = int(input("sayi 1: "))
sayi_2 = int(input("sayi 2: "))

carpim = sayi_1 * sayi_2
toplam = x + y + z
fark = carpim - toplam

print(f'sayiların carpimi: {carpim}, sayilarin toplami: {toplam}, sayilarin farki: {fark}')

#2- y' NİN x'E KALANSIZ BÖLÜMÜNÜ HESAPLAYINIZ.

print(y//x)

#3- (x,y,z) TOPLAMININ MOD 3' Ü NEDİR?

mod = toplam % 3
print(mod)

#4- y' NİN x. KUVVETİNİ HESAPLAYINIZ.

print(y**x)

#5- x, *y, z = NUMBERS İŞLEMİNE GÖRE z' NİN KÜPÜ KAÇTIR?

x, *y, z = numbers
print(x,y,z)
print(f'z nin küpü: {z**3}')

#6- x, *y, z = NUMBERS İŞLEMİNE GÖRE y' NİN DEĞERLERİ TOPLAMI KAÇTIR?

x, *y, z = numbers
print(f'y değerleri toplamı {y[0]+y[1]+y[2]}')