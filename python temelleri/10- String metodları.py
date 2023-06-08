message = 'Hello there. My name is  Sadık Turan'

message = message.upper() # STRING IFADENIN HEPSINI BUYUK HARF YAPAR
message = message.lower() # STRING IFADENIN HEPSINI KUCUK HARF YAPAR
message = message.title() # KELİMELERİN SADECE BAŞ HARFLERİNİ BÜYÜK HARF OLARAK YAZAR
message = message.capitalize() # CÜMLENİN SADECE İLK HARFİNİ BÜYÜK YAPAR GERİYE KALANLARI KÜÇÜK HARF OLARAK YAZAR
message = message.strip() # İÇİNE GİRİLEN KARAKTERİ SİLER
message = message.split() # HER BİR KELİME AYRI AYRI BİR DİZİ ŞEKLİNİ ALIR STRINGI PARÇALARA AYIRIR.
message = ' '.join(message) #ELEMANLAR ARASINA BOŞLUK VB. EKLER
message = message.replace('there', 'Yavuzhan') # ELEMAN DEĞİŞTİRME İŞLEMİ YAPAR
message = message.center(100) # İÇİNE GİRİLEN KARAKTER SAYISI KADAR SAĞDAN VE SOLDAN BOŞLUK BIRAKIR VE ORTALAMA İŞLEMİ YAPAR.


print(message.find('there')) # İÇİNE GİRİLEN DEĞERİN İNDEX BAŞLANGIÇ DEĞERİNİ VERİR.
print(message.endswith('H')) # İÇİNE GİRİLEN DEĞER İLE Mİ BİTİYOR? BİTİYOR İSE TRUE DEĞİL İSE FALSE DÖNDÜRÜR


print(message)