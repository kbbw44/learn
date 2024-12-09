# Задача 7
# Даны две строки из неповторяющихся символов first_string и second_string.
# Первая строка first_string длиной 3 символа. Вторая строка second_string точно содержит символы первой строки в любом порядке.
# Внутри функции minimum_length_slice напишите код - без использования циклов и условий, который находит срез минимальной длины во второй строке, содержащий все символы первой строки.
#
# Входные данные:
#
# строка first_string - строка длиной 3 символа
# Например, first_string='wtf'
# строка second_string - содержит символы первой строки в любом порядке
# Например, second_string='brick quz jmpy veldt whangs fox'
# Символы первой строки здесь - 'brick quz jmpy veldt whangs fox'
# Выходные данные:
#
# строка min_slice - срез минимальной длины во второй строке second_string, содержащий все символы первой строки first_string.
# Например, min_slice='t whangs f'

def minimum_length_slice(first_string, second_string):
    """Срез минимальной длины
    :param first_string: первая строка
    :param second_string: вторая строка
    :return: min_slice срез минимальной длины строки second_string
    """
    # todo Здесь нужно написать код
    first_string = 'wtf'
    second_string = 'brick quz jmpy veldt whangs fox'

    w1 = second_string.find(first_string[0])
    w2 = second_string.find(first_string[1])
    w3 = second_string.find(first_string[2])

    min_id = min(w1, w2, w3)
    max_id = max(w1, w2, w3)

    min_slice = second_string[min_id:max_id+1]

    return min_slice
