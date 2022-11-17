def greet():
    print("Добро пожаловать в телефонный справочник или что-то такое!")
    print()


def action():
    print("Выберите операцию:")
    print("1 - Вывести справочник")
    print("2 - Найти контакты по части имени")
    print("3 - Добавить контакт")
    print("4 - Отредактировать контакт")
    print("5 - Удалить контакт")
    print("6 - Экспортировать данные")
    print("7 - Импортировать данные")
    print("0 - закончить работу со справочником")
    print("Для выбора введите номер операции!")
    print()
    n = input()
    return n


def seek():
    print("Введите ФИО контакта целиком или частично!")
    print("Для отмены введите '0'")
    print()
    n = input()
    return n


def adding():
    N = ["",""]
    print("Введите ФИО нового контакта!")
    print("Для отмены введите '0'")
    print()
    N[0] = input()
    if N[0] == "0":
        return "0"
    print("Введите телефонный номер нового контакта!")
    print("Для отмены введите '0'")
    print()
    N[1] = input()

    if N[1] == "0":
        return "0"
    return N


def addingfin():
    print("Контакт успешно добавлен")
    print()


def redacter1():
    print("Введите ФИО контакта целиком!")
    print("Для отмены введите '0'")
    print()
    n = input()
    return n


def redacter2():
    N = ["",""]
    print(
        "Введите нвоое ФИО контакта или напишите '-1' если хотите оставить его прежним!"
    )
    print("Для отмены введите '0'")
    print()
    N[0] = input()

    if N[0] == "0":
        return "0"
    print(
        "Введите новый телефонный номер контакта или напишите '-1' если хотите оставить его прежним!"
    )
    print("Для отмены введите '0'")
    print()
    N[1] = input()
    if N[1] == "0":
        return "0"
    return N


def redacterfin():
    print("Контакт успешно изменен")
    print()


def deleter():
    print("Введите ФИО контакта целиком!")
    print("Для отмены введите '0'")
    print()
    n = input()
    return n


def deleterfin():
    print("Контакт успешно удален")
    print()


def exporter1():
    print("Выберите формат экспорта:")
    print("1 - .txt")
    print("2 - .CSV")
    print("3 - .JSON")
    print("Для отмены введите '0'")
    print()
    n = input()
    return n


def exporter2():
    print("Введите путь сохранения файла!")
    print("Для отмены введите '0'")
    print()
    n = input()
    return n


def exporterfin():
    print("Данные успешно экспортированы")
    print()


def importer1():
    print("Выберите формат экспорта:")
    print("1 - .txt")
    print("2 - .CSV")
    print("3 - .JSON")
    print("Для отмены введите '0'")
    print()
    n = input()
    return n


def importer2():
    print("Введите путь к файлу!")
    print("Для отмены введите '0'")
    print()
    n = input()
    return n


def importerfin():
    print("Данные успешно импортированы")
    print()


def operationend():
    print("Что делать дальше:")
    print("1 - вернуться к выбору операций")
    print("0 - закончить работу со справочником")
    print()
    n = input()
    return n


def end():
    print("Спасибо за выбор этой программы, хорошего дня!")
    print("^_^")
    print()

