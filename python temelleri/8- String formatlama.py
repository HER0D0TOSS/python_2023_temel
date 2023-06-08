
name = 'Yavuzhan'
surname = 'Ozgen'
age = 23

print('my name is {} {}'.format(name, surname))
print('my name is {1} {0}'.format(name, surname))
print('my name is {s} {n}'.format(n = name, s = surname))
print('my name is {s} {s}'.format(n = name, s = surname))
print('my name is {} {} and I am {} years old'.format(name, surname, age))
print('my name is {} {} and I am {} years old'.format(name, surname, 23))
print(f'my name is {name} {surname} and I am {age} years old') #fstring metodu

result = 200 / 700
print('the result is {}'.format(result))
print('the result is {r:1.3}'.format(r=result)) #  ondalk yuvarlama yapar