from os import path

file_base = 'base.txt'

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

# -----------------------
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
# -------------------------


def add_new_contact():
    global last_id

    array = ["surname", "name", "patronymic", "phone_number"]
    string = ""

    for i in array:
        string += input(f"Enter {i}: ") + " "
    last_id += 1

    with open(file_base, 'a', encoding="utf-8") as f:
        f.write(f"{last_id} {string}\n")


# ------------------------
# Решение ДЗ - Удаление контакта
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

# ------------------------


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
                pass
            case "5":
                del_contact(input("Какой контакт будем удалять? ").lower())
            case "6":
                pass
            case "7":
                play = False
            case _:
                print("Try again!\n")


main_menu()
