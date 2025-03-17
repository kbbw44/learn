# Задача 2
# Напишите класс PersonInfo.
#
# Экземпляр класса создается из следующих атрибутов:
# Строка - "Имя Фамилия";
# Число - возраст сотрудника;
# Подразделения - от головного до того, где работает сотрудник.
#
# Реализуйте методы класса:
# short_name, который возвращает строку Фамилия И.
# path_deps - возвращает путь "Головное подразделение --> ... --> Конечное подразделение"
# new_salary - Директор решил проиндексировать зарплаты, и новая зарпалата теперь вычисляется по формуле:
# 1337*Возраст*суммарное кол-во вхождений трех наиболее часто встречающихся букв из списка подразделений
# Регистр букв имеет значение. "А" и "а" - разные буквы.
#
# Пример: (Ввод --> Вывод)
# PersonInfo('Александр Шленский',32, 'Разработка', 'УК', 'Автотесты').short_name() --> 'Шленский А.'
# PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты').path_deps() --> 'Разработка --> УК --> Автотесты'
# # т.к. буква "т" встречается 4 раза, "а" - 3 раза, 'о' - 2 раза, остальные - по одной,
# # то сумма трёх самых частых букв равна 4+3+2 = 9.
# # Итого по формуле 1337*32*9 = 385056
# PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты').new_salary() --> 385056

class PersonInfo:
    def __init__(self, fi, age, *deps):
        self.fi = fi
        self.age = age
        self.deps = deps

    def short_name(self):
        """Краткая запись Фамилия И."""
        # todo Здесь нужно написать код
        fi = list(self.fi.split())
        return f'{fi[1]} {fi[0][0]}.'

    def path_deps(self):
        """Путь до подразделения"""
        # todo Здесь нужно написать код
        return (' --> '.join(self.deps))

    def new_salary(self):
        """Новая зарплата"""
        # todo Здесь нужно написать код
        salary_str = ''.join(self.deps)
        letters = {}
        letters_value = 0
        counter_end = 1
        for letter in salary_str:
            count = salary_str.count(letter)
            letters[letter] = count
        while counter_end <= 3:
            key_max = max(letters, key=letters.get)
            value_max = letters[key_max]
            letters_value += value_max
            del letters[key_max]
            counter_end += 1
        return 1337 * self.age * letters_value

