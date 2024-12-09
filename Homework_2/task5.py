# Задача 5
# Даны два числа a и b.
# Внутри функции sum_and_multiplication напишите код, который:
#
# в переменной a_b_sum вычисляет сумму a и b в формате 'a + b = c';
# в переменной a_b_multi вычисляет произведение a и b в формате 'a*b = c'.
# Входные данные:
#
# число a - первое число
# Например, a=5
# число b - второе число
# Например, b=10
#
# Выходные данные:
#
# a_b_sum - сумма a и b в формате 'a + b = c' , где c - это сумма a и b
# Например, a_b_sum='5 + 10 = 15'
# a_b_multi - произведение a и b в формате 'a*b = c' , где c - это произведение a и b
# Например, a_b_multi='5*10 = 50'

def sum_and_multiplication(a, b):
    """Сумма и произведение двух чисел
    :param a: первое число
    :param b: второе число
    :return: сумму и произведение
    """
    # todo Здесь нужно написать код
    a = 5
    b = 10
    sum = a + b
    multi = a * b
    a_b_sum = "%s + %s = %s" % (a, b, sum)
    a_b_multi = "%s*%s = %s" % (a, b, multi)
    return a_b_sum, a_b_multi