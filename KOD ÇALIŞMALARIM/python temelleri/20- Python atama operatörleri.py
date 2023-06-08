x, y, z = 5, 10, 15

#x,y = y,x

x += 5    # x = x + 5
x -= 5    # x = x - 5
x *= 5    # x = x * 5
x /= 5    # x = x / 5
x %= 5    # x = x % 5
x //= 5   # x = x // 5
x **= 5   # x = x ** 5


values = (1, 2, 3, 4, 5)

a, b, *c = values # a değeri =1, b değeri = 2 , c değeri ise önüne * koyuldugu için 3,4,5 in hepsini alır

print(a, b, c)
