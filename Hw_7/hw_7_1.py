# Задача 1 - Написать программу, которая проверяет есть ли в стихах Ритм. Стихотворение  вводится с с клавиатуры.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.
# Ритм есть, если число слогов (т.е. число гласных букв) в каждой Фразе стихотворения одинаковое
# В ответе напишите “Парам пам-пам” - если Ритм есть и “Пам парам” - если Ритма нет

# Пример:
# Ввод: пара-ра-рам рам-пам-папам па-ра-па-да
# Вывод: Парам пам-пам


letters = {'а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е'}


def is_ritm(list_text, list_let):
    count = []
    for i in list_text:
        count_i = 0
        for j in i:
            count_i += sum([int(j.count(l)) for l in list_let])
        count.append(count_i)
    return count


print("Напишите стихотворение: ")
poem = set(input().lower().split())
# print(poem)  # для проверки

res = set(is_ritm(poem, letters))
if len(res) == 1 and 0 not in res:
    print("Парам пам-пам")  # = OK = Ритм есть
else:
    print("Пам парам")  # = NO = Ритма нет

# print(is_ritm(poem, letters))  # для проверки

# print(res)  # для проверки


# рабочее
# --------------------------------
# for i in poem:
#     for j in i:
#         print(j, end=" ")
#     print()

# --------------------------------
# print([l for l in letters])

# --------------------------------
# count = []

# for i in poem:
#     count_i = 0
#     for j in i:
#         count_i += sum([int(j.count(l)) for l in letters])
#     count.append(count_i)
#     # print(count_i) # для проверки

# print(count)
