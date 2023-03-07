# Задача 1 - Вычислить, сколько раз встречается некоторое число X в массиве A[1..N].

count = int(input("Сколько элементов в массиве? "))
num = int(input("Какое число ищем в массиве? "))
# list_arr = []

print("Введите числа массива: ")

# 1й вариант (ограничено числом элементов в массиве)
list_arr = [int(input()) for i in range(count)]
print(list_arr)
print(sum(list_arr[i] == num for i in range(count)))


# 2й вариант (в этом случае нет необходимости спрашивать сколько элементов в массиве - он сразу их вводит)
# list_arr = [int(i) for i in input().split()]
# print(list_arr)
# print(sum(list_arr[i] == num for i in range(len(list_arr))))
