# Задача 2
# Дана функция global_function с локальной переменной msg = 1. Дополните логику функции следующим образом:
# 
# global_function должна содержать в себе функцию local_function;
# local_function должна изменить значение переменной msg на 2.


def global_function():
    """Нелокальные изменения
    :return: msg
    """
    msg = 1

    def local_function():
        pass
        # todo Здесь нужно написать код
        nonlocal msg
        msg = 2

    local_function()
    return msg
