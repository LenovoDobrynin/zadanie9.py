a1 = float(input('Введите число а1: '))
a2 = float(input('Введите число a2: '))
a3 = float(input('Введите число a3: '))
b1 = float(input('Введите число b1: '))
b2 = float(input('Введите число b2: '))
b3 = float(input('Введите число b3: '))
c1 = float(input('Введите число c1: '))
c2 = float(input('Введите число c2: '))
c3 = float(input('Введите число c3: '))
d1 = float(input('Введите число d1: '))
d2 = float(input('Введите число d2: '))
d3 = float(input('Введите число d3: '))
delta = a1*b2*c3+b1*c2*a3+c1*a2*b3-c1*b2*a3-a1*c2*b3-b1*a2*c3
if delta == 0:
    print('Главный определитель системы равен нулю')
else:
    delta1 = d1*b2*c3+b1*c2*d3+c1*d2*b3-c1*b2*d3-d1*c2*b3-b1*d2*c3
    delta2 = a1*d2*c3+d1*c2*a3+c1*a2*d3-c1*d2*a3-a1*c2*d3-d1*a2*c3
    delta3 = a1*b2*d3+b1*d2*a3+d1*a2*b3-d1*b2*a3-a1*d2*b3-b1*a2*d3
    x = delta1/delta
    y = delta2/delta
    z = delta3/delta
    print(x,y,z)