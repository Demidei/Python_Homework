def greet():
    print("Добро пожаловать или что-то такое!")
    print()


def action():
    print("Выберите операцию:")
    print("1 - Вывести список отделов")
    print("2 - Вывести список сотрудников")
    print("3 - Вывести список сотрудников отдела")
    print("4 - Добавить отдел")
    print("5 - Добавить сотрудника")
    print("6 - Переместить сотрудника в другой отдел")
    print("7 - Уволить сотрудника")
    print("0 - закончить работу со справочником")
    print("Для выбора введите номер операции!")
    print()
    n = input()
    return n


def seek_depart():
    print("Введите название отдела или id отдела")
    print("Для отмены введите '0'")
    print()
    n = input()
    return n


def adding_depart():
    print("Введите название отдела")
    print("Для отмены введите '0'")
    print()
    n = input()
    return n

def adding_emp_name():
    print("Введите имя сотрудника")
    print("Для отмены введите '0'")
    print()
    n = input()
    return n

def adding_emp_salary():
    print("Введите зарплату сотрудника")
    print("Для отмены введите '0'")
    print()
    n = input()
    return n

def adding_depart_fin():
    print("Отдел успешно добавлен")
    print()

def adding_empl_fin():
    print("Сотрудник успешно добавлен")
    print()


def redacter1():
    print("Введите имя сотрудника или его id")
    print("Для отмены введите '0'")
    print()
    n = input()
    return n


def redacter2():
    print("Введите название отдела или id отдела в который вы хотите переместить сотрудника")
    print("Для отмены введите '0'")
    print()
    n = input()
    return n


def redacterfin():
    print("Контакт успешно изменен")
    print()


def deleter():
    print("Введите имя сотрудника или его id")
    print("Для отмены введите '0'")
    print()
    n = input()
    return n



def deleterfin():
    print("Сотрудник успешно удален")
    print()





def operationend():
    print()
    print("Что делать дальше:")
    print("1 - вернуться к выбору операций")
    print("0 - закончить работу со справочником")
    print()
    n = input()
    return n


def end():
    print()

    print("Спасибо за выбор этой программы, хорошего дня!")
    print("^_^")
    print()

