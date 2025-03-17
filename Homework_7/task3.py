# Задача 3
# Реализовать три класса.
#
# I. Напишите класс PublicTransport.
# Экземпляр класса создается из следующих атрибутов:
# brand - Марка транспорта;
# ЗАЩИЩЕННЫЙ (protected) атрибут engine_power - Мощность двигателя;
# year - Год выпуска;
# color - Цвет;
# max_speed - Максимальная скорость.
# У класса должно быть свойство info, которое выводит на печать информацию о марке, цвете, годе выпуска и мощности двигателя.
#
# II. Напишите класс Bus, унаследованный от PublicTransport.
# Дополнительными атрибутами будут:
# passengers - количество пассажиров;
# ПРИВАТНЫЙ (private) атрибут park - Парк приписки автобуса;
# ЗАЩИЩЕННЫЙ (protected) атрибут fare - Стоимость проезда.
# Добавить свойство park, которое будет возвращать значение park, а при присвоении проверять номер парка, что он в диапазоне от 1000 до 9999. Если номер парка не попадает в диапазон, то выдавать ошибку.
#
# III. Напишите класс Tram, унаследованный от PublicTransport.
# Дополнительными атрибутами будут:
# ПРИВАТНЫЙ (private) атрибут route - маршрут трамвая;
# path - длина маршрута;
# ЗАЩИЩЕННЫЙ (protected) атрибут fare - Стоимость проезда.
# У класса должно быть свойство how_long, которое вычисляет время прохождения маршрута по формуле max_speed/(4*path)

class PublicTransport:
    def __init__(self, brand, engine_power, year, color, max_speed):
        pass
        # todo Здесь нужно написать код
        self.brand = brand
        self._engine_power = engine_power
        self.year = year
        self.color = color
        self.max_speed = max_speed

    @property
    def info(self):
        """Информация о транспорте"""
        # todo Здесь нужно написать код
        return


class Bus(PublicTransport):
    def __init__(self, brand, engine_power, year, color, max_speed, passengers, car_park, fare):
        super().__init__(brand, engine_power, year, color, max_speed)
        pass
        # todo Здесь нужно написать код
        self.passengers = passengers
        self.__park = car_park
        self._fare = fare

    @property
    def park(self):
        """Парк приписки автобуса"""
        # todo Здесь нужно написать код
        return self.__park

    @park.setter
    def park(self, value):
        assert 1000 <= value <= 9999
        self.__park = value

class Tram(PublicTransport):
    def __init__(self, brand, engine_power, year, color, max_speed, route, path, fare):
        super().__init__(brand, engine_power, year, color, max_speed)
        # todo Здесь нужно написать код
        self.__route = route
        self.path = path
        self._fare = fare

    @property
    def how_long(self):
        """Время прохождения маршрута"""
        # todo Здесь нужно написать код
        return ((self.max_speed) / (4 * self.path))
