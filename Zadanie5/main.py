import math
x = int(input('Введите длину первого катета: '))
y = int(input('Введите длину второго катета: '))
gip = math.sqrt(x**2 + y**2)
per = x + y + gip
pol = per/2
s = math.sqrt(pol*(pol-x)*(pol-y)*(pol-gip))
print(str(s)+ ' Площадь треугольника')
print(str(per) + " Периметр треугольника")