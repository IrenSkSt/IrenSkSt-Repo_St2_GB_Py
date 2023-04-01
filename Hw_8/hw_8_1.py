import os
from os import path

file_base = 'base.txt'
file_exp = 'My_Phone_book.txt'

last_id = 0
all_data = []


if not path.exists(file_base):
    with open(file_base, 'w', encoding="utf-8") as _:
        pass


def read_records():
    global last_id, all_data

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])
            return all_data
    return []


def show_all():
    global all_data
    # print(all_data)  # для проверки
    if all_data:
        print(*all_data, sep="\n")
    else:
        print("Empty data")

# -----------**------------
# Решение ДЗ - ПОИСК НУЖНОГО контакта для просмотра (п.3 меню = Serch)
# /!!! реализовано пока на полное совпадение со строкой поиска/Напр.: Иван, 123456, иван петрович/


def show_contact(search_str):
    global all_data

    contact = []

    # print(all_data)  # для проверки
    for i in all_data:
        # print(i)  # для проверки
        item = i.lower().split()
        for j in item:
            if j == search_str:
                contact.append(i)

    if len(contact) != 0:
        print(*contact, sep="\n")

    else:
        print("Такого контакта не найдено")
# -----------***--------------


def add_new_contact():
    global last_id

    array = ["surname", "name", "patronymic", "phone_number"]
    string = ""

    for i in array:
        string += input(f"Enter {i}: ") + " "
    last_id += 1

    with open(file_base, 'a', encoding="utf-8") as f:
        f.write(f"{last_id} {string}\n")


# -----------**-------------
# Решение ДЗ - Удаление контакта
# /!!! реализовано пока на полное совпадение со строкой поиска контакта для удаления/ Напр.: bin

def del_contact(search_str):
    global all_data

    contact_del = []
    accept = ""

    # print(all_data)  # для проверки
    for i in all_data:
        # print(i)  # для проверки
        item = i.lower().split()
        for j in item:
            if j == search_str:
                print("Вы хотите удалить этот контакт?")
                print(*i)
                accept += input("Да/Нет (Y/N):  ").upper()
                contact_del = i
                # print(contact_del)  # для проверки

                match accept:
                    case "Y" | "ДА":
                        # print("Удален: ")
                        all_data.pop(all_data.index(i))
                        # all_data.remove(i)
                        # return contact_del
                        # return
                    case "N" | "НЕТ":
                        contact_del = []
                    case _:
                        print("Try again!\n")

    if len(contact_del) != 0:

        with open(file_base, 'w', encoding="utf-8") as f:
            for i in all_data:
                f.write(f"{i}\n")

        # print(all_data)  # для проверки
        print("Этот контакт удален: ")
        print(*contact_del)
        contact_del = []
    else:
        print("Контакт для удаления не найден")
# -----------***-------------


# ------------**------------
# Решение ДЗ - Изменение контакта
# /!!! реализовано пока на полное совпадение со строкой поиска контакта для измения/ Напр.: name

def insert_contact(search_str):
    global all_data

    array = ["surname", "name", "patronymic", "phone_number"]
    contact_ins = ""
    accept = ""

    # print(all_data)  # для проверки
    for i in all_data:
        # print(i)  # для проверки
        item = i.lower().split()
        for j in item:
            if j == search_str:
                print("Вы хотите изменить этот контакт?")
                print(*i)
                accept += input("Да/Нет (Y/N):  ").upper()
                contact_ins = i
                # print(contact_ins)  # для проверки

                match accept:
                    case "Y" | "ДА":
                        id = contact_ins.split()[0]
                        # print(id)  # для проверки
                        i_new = id + " "
                        for m in array:
                            i_new += input(f"Enter {m}: ") + " "
                        all_data[all_data.index(i)] = i_new

                    case "N" | "НЕТ":
                        contact_ins = ""
                    case _:
                        print("Try again!\n")

    if len(contact_ins) != 0:

        with open(file_base, 'w', encoding="utf-8") as f:
            for i in all_data:
                f.write(f"{i}\n")

        # print(all_data)  # для проверки
        print("Контакт изменен на: ")
        print(*i_new)
        contact_ins = ""
    else:
        print("Контакт для изменения не найден")
# -------------***-----------


# -----------**-------------
# Решение ДЗ - Экспорт/Выгрузка телефонной книги в файл

def export_contact_list():
    global all_data

    with open(file_exp, 'w', encoding="utf-8") as f:
        for i in all_data:
            f.write(f"{i}\n")
    print("Список Ваших контактов выгружен в файл: My_Phone_book.txt ")
# -----------***-------------


# -----------**-------------
# Решение ДЗ - Импорт/Загрузка контактов в телефонную книгу из другого файла: Contacts.txt
# (имитация переноса с другого телефона без проверки дубликатов)

def import_contact_list(add_file):
    global last_id, all_data
    new_data = []

    with open(add_file, 'r', encoding="utf-8") as f:
        new_data = [item.strip() for item in f]
    # print(new_data)  # для проверки

    for item in new_data:
        last_id += 1

        # item = item.strip()[1:]
        # print(item) # для проверки
        all_data.append(f"{last_id} {item.strip()[1:]}")

    # print(all_data) # для проверки

    with open(file_base, 'w', encoding="utf-8") as f:
        for i in all_data:
            f.write(f"{i}\n")

    if len(new_data) != 0:
        print("В телевонную книгу добавлены новые контакты: ")
        print(*new_data)
    else:
        print("Что-то пошло не так: новые контакты не были добавлены в телефонную книгу")
# -----------***-------------


def main_menu():
    play = True

    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Change\n"
                       "5. Delete\n"
                       "6. Exp/Imp\n"
                       "7. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                show_contact(input("Search: ").lower())
            case "4":
                insert_contact(input("Какой контакт будем изменять? ").lower())
            case "5":
                del_contact(input("Какой контакт будем удалять? ").lower())
            case "6":
                choice = input(
                    "Выгрузить Список контактов в файл? (Y/N) ").upper()
                if choice == "Y":
                    export_contact_list()
                elif choice == "N":
                    choice = input(
                        "Загрузить Список контактов в файл? (Y/N) ").upper()
                    if choice == "Y":
                        # print(os.path.basename(
                        #     input("Укажите путь к файлу Contacts.txt для импорта контактов: ")))  # для проверки
                        import_contact_list(os.path.basename(
                            input("Укажите путь к файлу Contacts.txt для импорта контактов: ")))
                        # pass

                else:
                    print("Try again!\n")
            case "7":
                play = False
            case _:
                print("Try again!\n")


main_menu()
