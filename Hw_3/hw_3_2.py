# Задача 2 - Найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X

count = int(input("Сколько элементов в массиве? "))
num = int(input("Укажите число: "))
min = 0


print("Введите числа массива: ")
list_arr = [int(input()) for i in range(count)]
print(list_arr)
item_min = list_arr[0]

for i in range(len(list_arr)):
    if abs(num - list_arr[i]) <= min:
        item_min = list_arr[i]
        min = abs(num - list_arr[i])

print(f"Ближайший элемент к заданному числу = {item_min}")
