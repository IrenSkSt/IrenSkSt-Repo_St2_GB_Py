# Задача 1 - Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

def num_round(num_a, num_b):
    if num_b == 0:
        return 1
    return num_a * num_round(num_a, num_b-1)


num = int(input("Укажите число: "))
r = int(input("Укажите степень для возведения в него числа: "))

print(f"{num} в степени {r} = {num_round(num, r)}")
