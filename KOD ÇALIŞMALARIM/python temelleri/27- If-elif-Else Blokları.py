#           ELIF BLOĞU          #
#
# Bazen birden fazla koşul yazmak isteriz bu durumda eğer ilk if bloğundaki koşul False değer üretirse Elif bloğunda tanımladığımız koşula bakılır.


a = 10
b = 10
if b > a:
  print("b, a'dan büyüktür")
elif a == b:
  print("a ile b eşittir")


a = 15
b = 10
if b > a:
  print("b, a'dan büyüktür")
elif a == b:
  print("a ile b eşittir")
else:
  print("a, b'den büyüktür")