def add_contact():
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone = input("Введите номер телефона: ")

    contact = f"{surname} {name} {patronymic}: {phone}"

    with open("contacts.txt", "a", encoding='utf-8') as file:
        file.write(contact + "\n")
        file.write('\n')

def search_by_surname():
    surname = input("Введите фамилию для поиска: ")
    found_contacts = []

    with open("contacts.txt", "r", encoding='utf-8') as file:
        for line in file:
            contact = line.strip()
            if contact.split(" ")[0] == surname:
                found_contacts.append(contact)

    if len(found_contacts) > 0:
        print("Найденные контакты:")
        for contact in found_contacts:
            print(contact)
    else:
        print("Контакты с такой фамилией не найдены")