# Задача 1 - На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

count = int(input("Количество монеток на столе? "))
min = 0
result = 0

for i in range(count):
    temp = int(input("орёл (=1) или решка (=0)? "))
    if temp == 0:
        result += 1
if count - result < result:
    min = count - result
else:
    min = result

print(min)
