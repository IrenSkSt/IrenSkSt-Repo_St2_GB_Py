# Задача 1 - Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь задает размер множеств и значения множеств.

n = int(input("Размер 1-го набора чисел: "))
m = int(input("Размер 2-го набора чисел: "))
list_1 = []
list_2 = []

print("Введите целые числа для формирования наборов: ")
for i in range(n+m):
    if i < n:
        list_1.append(int(input()))
    else:
        list_2.append(int(input()))
# print(list_1)  # для проверки
# print(list_2)  # для проверки

my_set = list(set(list_1).union(set(list_2)))
# print(my_set)  # для проверки

# 1й вариант решения:
for i in reversed(my_set):
    print(i, end=" ")

print()

# ------------------------------------
# 2-й вариант решения:

# while len(my_set) > 1:
#     for i in my_set:
#         print(max(my_set), end=" ")
#         my_set.remove(max(my_set))
#         # print(my_set)  # для проверки

# print(my_set[0])
