# Задача 2 - Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

d1 = int(input("Укажите нижний порог диапазона: "))
d2 = int(input("Укажите верхний порог диапазона: "))
n = int(input("Количество чисел в массиве: "))

list_rand = [random.randint(-10, 20) for _ in range(n)]
print(list_rand)

print("Индексы элементов, которые соответствуют диапазону: ")
ind = [i for i, v in enumerate(list_rand) if d1 <= v <= d2]
print(ind)

# print([i for i, v in enumerate(list_rand) if d1 <= v <= d2])


# развернутая версия
# for i, v in enumerate(list_rand):
#     if d1 <= v <= d2:
#         print(i, end=" ")
