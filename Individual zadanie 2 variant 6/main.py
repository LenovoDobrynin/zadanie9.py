import math
x= int(input('x= '))
y= int(input('y= '))
z = int(input('z= '))
try:
    a = (2 * math.cos(x - math.pi/6 ))/(1/2 + math.sin(y)**2)
except ZeroDivisionError:
    print('Деление на ноль')
else:
    print(a)
try:
    b = 1 + ((z ** 2) / (3 + ((z ** 2) / 5)))
except ZeroDivisionError:
    print('Деление на ноль')
else:
    print(b)
