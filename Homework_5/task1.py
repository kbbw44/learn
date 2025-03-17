# Задача 1
# Напишите функцию letter_stat, которая на вход принимает строку our_str и возвращает словарь letters_dict,
# где в качестве ключей - буквы строки, а значениями являются числа, соответствующие количеству вхождений данной буквы в строку.
#
# Входные данные:
# строка типа str
# Например, our_str='letter'
#
# Выходные данные:
# словарь типа dict
#
# Пример:
# letter_stat('letter') --> {'l': 1, 'e': 2, 't': 2, 'r': 1}

def letter_stat(our_str):
    """Буквенная статистика
    :param our_str: строка
    :return: словарь со статистикой по буквам
    """
    # todo Здесь нужно написать код
    str_list = list(our_str)
    letters_dict = {}
    for i in range(len(str_list)):
        letters_dict.setdefault(str_list[i], str_list.count(str_list[i]))
    return letters_dict

