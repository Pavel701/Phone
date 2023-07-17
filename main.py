from filling_directory import add_contact, search_by_surname


def main():
    while True:
        print("1. Добавить контакт")
        print("2. Поиск контакта по фамилии")
        print("3. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_by_surname()
        elif choice == "3":
            break
        else:
            print("Некорректный ввод")



main()