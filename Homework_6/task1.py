# Задача 1
# Имеются две переменные, определенные в глобальной области видимости модуля:
# number = 1
# string = 'Hello'
# Напишите функцию global_changes, которая будет изменять и возвращать эти переменные со следующими значениями:
# number = 5
# string = 'Hello, dear friend'

number = 1
string = 'Hello'


def global_changes():
    """Глобальные переменные
    :return: number, string
    """
    # todo Здесь нужно написать код
    global number
    global string
    number = 5
    string = 'Hello, dear friend'
    return number, string
