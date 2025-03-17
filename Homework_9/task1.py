# Задача 1
# Дан текстовый файл "test_file/task1_data.txt".
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры, создать файл "test_file/task1_answer.txt" и записать в него получившийся текст.
# 
# Входные данные:
# "test_file/task1_data.txt" - путь до файла с исходными данными
# 
# Выходные данные:
# файл "test_file/task1_answer.txt" с итоговыми данными.

# todo Здесь нужно написать код
f = open('test_file/task1_data.txt', encoding='utf-8').read()
with open('test_file/task1_answer.txt', mode='a+', encoding='utf-8') as new_f:
    for char in f:
        if char.isdigit() == True:
            pass
        else:
            new_f.write(char)


