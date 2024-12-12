# Задача 3
# Напишите функцию even_sum, которая принимает список чисел lst и возвращает сумму элементов с четными индексами.
# 
# 
# Входные данные:
# 
# список типа list из чисел типа int
# Например, lst=[1, 2, 3, 4, 5, 6, 7]
# 
# Выходные данные:
# 
# число типа int
# 
# Пример:
# 
# # 1 + 3 + 5 + 7 = 16
# even_sum([1, 2, 3, 4, 5, 6, 7]) --> 16


def even_sum(lst):  
    """Получение суммы элементов списка с четными индексами
    :param lst: список из чисел
    :return: сумму элементов с четными индексами
    """
    # todo Здесь нужно написать код
    b = lst[::2]
    even_sum = int(sum(b))
    return even_sum
