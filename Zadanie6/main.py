num = int(input("Введите целое четырехзначное число: "))
if num <1000:
    print('Не четырехзначное число!')
elif num >9999:
    print('Не четырехзначное число!')
else:
    sum = 0
    while (num != 0):
        sum = sum + num % 10
        num = num // 10
    print("Сумма цифр числа равна: ", sum)