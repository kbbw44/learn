# Задача 6
# Напишите функцию create_phone_number, которая принимает кортеж num_tuple
# из 10 цифр и возвращает строку из этих цифр в виде номера телефона.
#
#
# Входные данные:
#
# кортеж типа tuple из цифр типа int
# Например, num_tuple=(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
#
# Выходные данные:
#
# строка типа str
#
# Пример:
#
# create_phone_number((1, 2, 3, 4, 5, 6, 7, 8, 9, 0)) --> "(123) 456-7890"

def create_phone_number(num_tuple):
    """Создание номера телефона
    :param num_tuple: кортеж из цифр
    :return: строку в виде номера телефона
    """
    # todo Здесь нужно написать код
    num_str = str(num_tuple)
    deleted_chars = ", ()"
    str_w_chars = ''.join(char for char in num_str if char not in deleted_chars)
    return("(" + (str_w_chars[0:3]) + ")" + " " + (str_w_chars[3:6]) + '-' + (str_w_chars[6:10]))

