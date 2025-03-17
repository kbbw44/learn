# Задача 3
# Дана функция get_kinetic_energy, которая вычисляет кинетическую энергию. В ней ничего изменять не нужно!
#
# Напишите декоратор memorize, который организует механизм кэширования данной функции.
# Декоратор должен сохранять информацию о вызове функции в словарь, в котором ключ - это аргументы,
# с которыми была вызвана функция, а значение - это результат выполнения функции.
# Если функция с такими аргументами вызывается впервые, то в словарь добавляется информация об этом вызове.
# Если функция с такими аргументами уже вызывалась, то новое значение в словарь не добавляется.
#
# Входные данные:
# число weight типа int - масса
# число speed типа int - скорость
#
# Выходные данные:
# кортеж типа tuple из двух элементов: результат
# вычисления кинетической энергии и словарь с информацией о вызовах функции

def memorize(func):
    # todo Здесь нужно написать код
    cached = {}
    def wrapper(*args, **kwargs):
        if args in cached:
            pass
        result_kinetic = func(*args)
        cached[args] = result_kinetic
        return result_kinetic, cached
    return wrapper



# todo Здесь ничего изменять не нужно!
@memorize
def get_kinetic_energy(weight, speed):
    """Кинетическая энергия
    :param weight: масса
    :param speed: скорость
    :return: кинетическую энергию
    """
    return (weight * speed ** 2)/2

