# Задача 3
# Напишите функцию segment.
# На вход подаются два кортежа с координатами точек (x1, y1), (x2, y2).
#
# Входные данные:
# первый кортеж типа tuple
# второй кортеж типа tuple
# В функции происходит проверка на корректность полученных данных.
# С помощью инструкции try/except as отлавливается исключение Exception.
# Если исключение поймано, то функция возвращает текст исключения наоборот.
# Например, исключение "unsupported operand type(s) for +: 'int' and 'str'" будет выглядеть
# наоборот как "'rts' dna 'tni' :+ rof )s(epyt dnarepo detroppusnu"
# Если исключения не произошло, то функция возвращает сумму всех координат.

def segment(first_point, second_point):
    """Сумма всех координат точек
    :param first_point: координаты первой точки
    :param second_point: координаты второй точки
    :return: текст исключения наоборот или сумму всех координат
    """
    # todo Здесь нужно написать код
    try:
        result = first_point[0] + second_point[0] + first_point[1] + second_point[1]
    except TypeError as e:
        return ''.join(reversed(str(e)))
    return result
