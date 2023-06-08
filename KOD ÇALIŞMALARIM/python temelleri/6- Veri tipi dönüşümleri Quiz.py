"""
    DAİRE ALANI  : πr**2
    DAİRE ÇEVRESİ : 2πr

    * Yarı çapı verilen bir dairenin  alan ve çevresini hesaplayınız. (r:3.14) 
    
"""


# ÇÖZÜM  #


pi = 3.14

yariCap = int(input("yaricap giriniz: "))

alan = pi * yariCap**2
cevre = 2*pi*yariCap

print(f'YARIÇAPI VERİLEN DAİRENİN ALANI: {alan}, ÇEVRESİ: {cevre}')
