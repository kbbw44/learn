# Задача 1
# Напишите класс Segment. Для его инициализации нужно два кортежа с координатами точек (x1, y1), (x2, y2).
# 
# Реализуйте методы класса:
# length, который возвращает длину нашего отрезка с округлением до 2 знаков после запятой;
# x_axis_intersection, который возвращает True, если отрезок пересекает ось абцисс, иначе - False;
# y_axis_intersection, который возвращает True, если отрезок пересекает ось ординат, иначе - False
# 
# Пример: (Ввод --> Вывод)
# Segment((2, 3), (4, 5)).length() --> 2.83
# Segment((-2, -3), (4, 5)).x_axis_intersection() --> True
# Segment((-2, -3), (-4, -5)).y_axis_intersection() --> False

import math

class Segment:
    def __init__(self, first_point, second_point):
        self.first_point = first_point
        self.second_point = second_point

    def length(self):
        """Вычисление длины отрезка"""
        # todo Здесь нужно написать код
        return round(math.sqrt((self.second_point[0] - self.first_point[0]) ** 2 + (self.second_point[1] - self.first_point[1]) ** 2), 2)

    def x_axis_intersection(self):
        """Пересечение оси абсцисс"""
        # todo Здесь нужно написать код
        if (self.second_point[1] > 0 > self.first_point[1]) or (self.second_point[1] > 0 > self.first_point[1]):
            if self.first_point[0] != self.second_point[0]:
                return True
        return False

    def y_axis_intersection(self):
        """Пересечение оси ординат"""
        # todo Здесь нужно написать код
        if (self.second_point[0] > 0 > self.first_point[0]) or (self.second_point[0] > 0 > self.first_point[0]):
            if self.first_point[1] != self.second_point[1]:
                return True
        return False
