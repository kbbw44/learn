# Задача 7
# Напишите функцию move_zeros, который принимает список lst и перемещает все нули
# в конец, сохраняя порядок остальных элементов.
#
# Входные данные:
#
# список типа list из цифр типа int
# Например, lst=[1, 0, 1, 2, 0, 1, 3]
#
# Выходные данные:
#
# список типа list
#
# Пример:
#
# move_zeros([1, 0, 1, 2, 0, 1, 3]) --> [1, 1, 2, 1, 3, 0, 0]

def move_zeros(lst):
    """Перемещение нулей
    :param lst: список из цифр
    :return: список из цифр с нулями в конце
    """
    # todo Здесь нужно написать код
    count_zero = 0
    for num in lst:
        if num == 0:
            count_zero += 1
    while 0 in lst:
        lst.remove(0)
    lst.extend([0] * count_zero)
    return lst
