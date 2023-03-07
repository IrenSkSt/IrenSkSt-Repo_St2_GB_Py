# Задача 3 - Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

limit = int(input("Укажите число: "))
around = 0
number = 2
result = 1
if limit < 1:
    print("Это число меньше 2 в 0й степени")

while result <= limit:
    print(f"{number}^{around} = {result}")
    result *= number
    around += 1
