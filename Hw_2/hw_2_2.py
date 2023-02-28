# Задача 2 - Петя загадывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

num_summ = int(input("Сумма 2х чисел: "))
num_mult = int(input("Произведение 2х чисел: "))
list_x = []
list_y = []

temp = (num_summ**2) - (4*num_mult)
print("D =", num_summ**2, " - ", 4*num_mult, " = ", temp)  # для проверки

if temp < 0:
    print("Таких чисел нет, Петя проверь сумму и произведение, загаданных чисел")
elif num_mult == 0:
    # вариант с нулем, хотя условия задачи подразумевают натуральные числа: 1, 2, 3, ... n
    print(f"Ответ: {num_summ} и 0 ")
else:
    x1 = int((num_summ + temp**(1/2))/2)
    y1 = int(num_summ-x1)
    i = 0
    print(x1, y1)  # для проверки

    if y1 != 0:
        list_x.append(x1)
        list_y.append(y1)
        i += 1

    if temp > 0:
        x2 = int((num_summ - temp**(1/2))/2)
        y2 = int(num_summ-x2)
        print(x2, y2)  # для проверки
        if y2 != 0:
            list_x.append(x2)
            list_y.append(y2)

for i in range(len(list_x)):
    print(f"Ответ {i+1}: {list_x[i]} и {list_y[i]}")

    print("Сумма = ", list_x[i] + list_y[i],
          "Произведение = ", list_x[i] * list_y[i])  # для проверки

print("x =", list_x, "y =", list_y)  # для проверки
