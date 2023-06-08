#           MANTIKSAL OPERATÖRLER           #


# Mantıksal operatörler birden fazla koşulu beraberce değerlendirmek için kullanılır


#1- AND(VE) OPERATÖRÜ
#
# Belirli koşulların hepsi doğru ise True, biri bile doğru değil ise False değeri döndürür

true = (6>5 and 5<6)
false = (4>5 and 4<5)

print(f'dogru değer: {true}')
print(f'Yanlış durum: {false}')


#2- OR(VEYA) OPERATÖRÜ 
#
# Bu operatörde her durumun doğru olmasına gerek yoktur. Durumlardan biri doğru olsa bile sonuç True döndürür. Hepsi yanlış ise False değeri döndürür.

true2 = (6>5 or 5<6)
true3 = (4>5 or 4<5)
false2 = (4>5 or 4<3)

print(f'dogru değer: {true2}')
print(f'dogru değer 2: {true3}')
print(f'Yanlış durum: {false2}')

#3- NOT(DEĞİL) OPERATÖRÜ
#
# Bu operatör ile koşulların tersi alınır. Örnek olarak değer bize True olarak dönüyorsa False, False olarak dönüyorsa True olarak geri döndürür.

x = 5
sonuc = not(x > 3 and x < 10)
print(sonuc)

x = 2
sonuc = not(x > 3 and x < 10)
print(sonuc)