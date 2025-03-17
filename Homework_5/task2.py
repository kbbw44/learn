# Задача 2
# Напишите функцию repeats, которая на вход принимает строку our_str, смотрит,
# сколько раз каждый символ уже встречался, и добавляет к символам постфикс вида _n. Возвращает новую строку.
#
# Входные данные:
# строка типа str
# Например, our_str='letter'
#
# Выходные данные:
# строка типа str
#
# Пример:
# repeats('letter') --> 'l_1e_1t_1t_2e_2_r_1'

def repeats(our_str):
    """Повторы букв
    :param our_str: строка
    :return: новая строка с повторами букв
    """
    # todo Здесь нужно написать код
    str_list = list(our_str)
    letters_dict = {}
    result = []
    for i in range(len(str_list)):
        letters_dict.setdefault(str_list[i], str_list.count(str_list[i]))
    for i in range(len(str_list)):
        result.append(str_list[i])
        result.append(f'_{str_list[:i + 1].count(str_list[i])}')
    result = ''.join(result)
    return result

