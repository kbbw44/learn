# Задача 4
# Напишите функцию multiplication_chain, которая принимает положительное число num и возвращает количество раз, которое вы должны перемножить цифры числа num и полученных произведений, пока не получите одну цифру.
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
# # num=39 --> 3*9 = 27, 2*7 = 14, 1*4 = 4, 4 - одна цифра, стоп. Итого 3 итерации, ответ - 3
# multiplication_chain(39) --> 3
# # num=999 --> 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, 1*2 = 2, 2 - одна цифра, стоп. Итого 4 итерации, ответ - 4
# multiplication_chain(999) --> 4
# # num=4 --> 4 - уже одна цифра, а значит мы проделали 0 итераций, ответ - 0
# multiplication_chain(4) --> 0

def multiplication_chain(num):
    """Цепочка умножений
    :param num: положительное число
    :return: количество перемножений
    """
    # todo Здесь нужно написать код
    count = 0
    while num >= 10:
        num_str = str(num)
        multi = 1
        for char in num_str:
            multi *= int(char)
        num = multi
        count += 1
    return count
