h = int(input("Введите количество часов: "))
m = int(input("Введите количество минут: "))
s = int(input("Введите количество секунд: "))
c = h * 30 + m * 30 / 60 + s * 30 / 3600
print(str(c) + " Градусов")

