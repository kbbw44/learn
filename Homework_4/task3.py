# Задача 3
# Напишите функцию sum_digits, которая принимает положительное число num и 
# возвращает сумму его цифр.
# 
# 
# Входные данные:
# 
# положительное число типа int
# Например, num=39
# 
# Выходные данные:
# 
# число типа int
# 
# Пример:
# 
# sum_digits(39) --> 12 # 3 + 9 = 12
# 
# sum_digits(999) --> 27 # 9 + 9 + 9 = 27
# 
# sum_digits(4) --> 4

def sum_digits(num):
    """Нахождение суммы цифр числа
    :param num: число
    :return: сумма цифр числа
    """
    # todo Здесь нужно написать код
    sum_digits = 0
    str_num = str(num)
    for char in str_num:
        sum_digits += int(char)
    return sum_digits



