# Задача 1
# Дана функция hello_world.
# Внутри этой функции:
#
# создайте переменную hello со значением 'Hello';
# создайте переменную world со значением 'world';
# в переменную hello_and_world запишите сумму переменных hello и world через пробел и в конце добавьте восклицательный знак.

def hello_world():
    """Привет, мир!"""

    # todo Здесь нужно написать код
    hello = 'Hello'
    world = 'world'
    hello_and_world = hello + " " + world + "!"
    return hello_and_world


