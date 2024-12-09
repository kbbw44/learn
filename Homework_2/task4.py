# Задача 4
# Дан абсолютный путь до файла file_path.
# Внутри функции test_file_path напишите код, который:
#
# в переменной file_name вычисляет название файла без расширения;
# в переменной disk_name вычисляет название диска;
# в переменной root_folder вычисляет корневую папку.
# Входные данные:
#
# строка file_path - абсолютный путь до файла
# Например, file_path=r'C:\Python311\python.exe'
# Выходные данные:
#
# file_name - название файла без расширения
# Например, file_name='python'
# disk_name - название диска
# Например, disk_name='C'
#
# root_folder - корневая папка
# Например, root_folder='Python311'

def test_file_path(file_path):
    """Путь до файла
    :param file_path: абсолютный путь до файла
    :return: название файла без расширения, названия диска и корневую папку
    """
    # todo Здесь нужно написать код
    file_path = r'C:\Python311\python.exe'
    file_name = file_path.split('\\')
    disk_name = file_path.split(':')
    root_folder = file_path.split('\\')
    return ((file_name[2].split('.')[0]), disk_name[0], root_folder[1])
