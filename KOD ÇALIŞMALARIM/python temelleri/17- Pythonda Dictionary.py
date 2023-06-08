#           DICTIONARY(SOZLUK)          #


# DEĞERLERİ KEY-VALUE ŞEKLİNDE TUTARLAR

sehirler = ['Kocaeli', 'İstanbul']
plakalar = [41, 34]

plakalar = {'Kocaeli': 41, 'İstanbul': 34}

print(plakalar['Kocaeli'])

plakalar['Ankara'] = 6
print(plakalar)

users = {
    'Sadikturan': {
        'age': 36,
        'email': 'wwww@gmail.com',
        'address':'kocaeli',
        'phone': 12312321
    },
    'Cinarturan':{
        'age':2,
        'email': 'none',
        'address': 'kocaeli',
        'phone': 'none'
    }
}


print(users['Sadikturan']['age'])
print(users['Cinarturan']['address'])
