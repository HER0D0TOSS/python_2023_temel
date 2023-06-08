#               LİSTE METODLARI             #


print(dir(list))

listem = [0, 1, 2, 3, 4, 5]
listem2 = [7, 10, 11, 12]

reversed(listem) # "reversed" FONKSİYONUNU BİR LİSTEYE UYGULARSAK BU BİZE list_reverseiterator ADI VERİLEN BİR NESNE ELDE EDERİZ.

listem.append(6) # LİSTEYE ELEMAN EKLEME İŞLEMİ YAPAR.
listem.extend(listem2) # LİSTEYE İKİNCİ BİR LİSTEYİ EKLER.
listem.insert(7, "altı") # VERİLEN İNDEX DEĞERİNE VERİLEN DEĞERİ ATAR.
listem.remove(12) # İÇİNE VERİLEN DEĞER EĞER LİSTEDE BULUNUYORSA SİLER.
listem.reverse() # LİSTEYİ TERS ÇEVİRİR.
listem.pop() # İÇİNE VERİLEN İNDEX DEĞERİNİ SİLER, İÇİNE DEGER VERİLMEZ İSE LİSTENİN SON ÖĞESİNİ SİLER.
listem.sort() # LİSTE ELEMANLARINI BERLİRLİ BİR KURALA GÖRE SIRALAMAMIZI SAĞLAR.
listem.index() # İÇİNE VERİLEN DEĞERİN İNDEX NUMARASINI BİZE VERİR.
listem.count() # İÇİNE VERİLEN DEĞERİN LİSTEDE KAÇ ADET BULUNDUGUNU BİZE GÖSTERİR.
listem.copy() # LİSTELERİ BİRBİRNE KOPYALAMAK İÇİN KULLANILIR.
listem.clear() # LİSTENİN İÇERİĞİNİ SİLER.

print(listem)