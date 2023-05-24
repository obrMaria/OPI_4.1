#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Составить программу с использованием классов и объектов для решения задачи.
Во всех заданиях, помимо указанных в задании операций, обязательно должны быть реализованы следующие методы:
    •	метод инициализации __init__ ;
    •	ввод с клавиатуры read ;
    •	вывод на экран display .
В раздел программы, начинающийся после инструкции if __name__ = '__main__': добавить код,
демонстрирующий возможности разработанного класса.
6.(21) Создать класс Point для работы с точками на плоскости. Координаты точки — декартовы.
Обязательно должны быть реализованы:
    перемещение точки по оси ,
    определение расстояния до начала координат,
    расстояния между двумя точками,
    преобразование в полярные координаты,
    сравнение на совпадение и несовпадение.
"""

import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def read(self):
        self.x = float(input("Введите значение координаты x: "))
        self.y = float(input("Введите значение координаты y: "))

    def display(self):
        print(f"Координаты точки: ({self.x}, {self.y})")

    def move_x(self, dx):
        self.x += dx

    def move_y(self, dy):
        self.y += dy

    def distance_to_origin(self):
        return math.sqrt(self.x**2 + self.y**2)

    def distance_to_point(self, other_point):
        dx = other_point.x - self.x
        dy = other_point.y - self.y
        return math.sqrt(dx**2 + dy**2)

    def to_polar_coordinates(self):
        r = math.sqrt(self.x**2 + self.y**2)
        theta = math.atan2(self.y, self.x)
        return r, theta

    def compare(self, other_point):
        return self.x == other_point.x and self.y == other_point.y


if __name__ == '__main__':
    point1 = Point()
    point1.read()
    point1.display()

    point2 = Point()
    point2.read()
    point2.display()

    point1.move_x(2)  # Перемещение точки point1 по оси x на 2 единицы
    point1.move_y(-1)  # Перемещение точки point1 по оси y на -1 единицу

    print("новые координаты перой точки: ")
    point1.display()  # Вывод новых координат точки point1

    distance_center = point1.distance_to_origin()
    print("Расстояние до центра от первой точки:", distance_center)

    distance = point1.distance_to_point(point2)
    print("Расстояние между точками:", distance)

    polar_coords = point1.to_polar_coordinates()
    print("Полярные координаты первой точки:", polar_coords)

    are_equal = point1.compare(point2)  # Сравнение точек point1 и point2 на совпадение
    if are_equal:
        print("Точки совпадают")
    else:
        print("Точки не совпадают")
