# Задача 6
# Дана строка string.
# Внутри функции delete_symbols напишите код, который:
#
# в переменной new_string удаляет символы, имеющие нечетные значения индекса заданной строки string.
# Входные данные:
#
# строка string
# Например, string='Hello World'
# Выходные данные:
#
# new_string - строка без символов с нечетными индексами исходной строки string.
# Например, new_string='HloWrd'

def delete_symbols(string):
    """Удаление символов с нечетными индексами
    :param string: строка
    :return: строку без символов с нечетными индексами исходной строки
    """
    # todo Здесь нужно написать код
    string = 'Hello World'
    new_string = string[0::2]
    return new_string
