# Задача 2
# Дан файл 'test_file/task_2.txt'. Можно считать, что это запись покупок в магазине, где указана только цена товара.
# В каждой строке файла записана цена товара.
# Покупки, т.е. несколько подряд идущих цен, разделены пустой строкой.
# Нужно найти сумму трех самых дорогих покупок и записать результат в переменную most_expensive_purchases.
# 
# Входные данные:
# 'test_file/task_2.txt' - путь до файла с записями покупок в магазине
# 
# Выходные данные:
# most_expensive_purchases - сумма трех самых дорогих покупок.

def three_most_expensive_purchases():
    """Три самые дорогие покупки
    :return: сумму трех самых дорогих покупок
    """
    file_path = "test_file/task_2.txt"
    # todo Здесь нужно написать код
    most_expensive_purchases = ""
    purchase_list = []
    current_purchase = []

    with open(file_path) as f:
        f_list = f.read().splitlines()
    for line in f_list:
        if line == '':
            if current_purchase:
                purchase_list.append(current_purchase)
                current_purchase = []
        else:
            current_purchase.append(int(line))

    purchase_sum = [sum(purchase) for purchase in purchase_list]
    most_expensive_purchases = (sum(sorted(purchase_sum, reverse=True)[:3]))
    return most_expensive_purchases
