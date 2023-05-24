#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Парой называется класс с двумя полями, которые обычно имеют имена first и second.
Требуется реализовать тип данных с помощью такого класса.
Во всех заданиях обязательно должны присутствовать:
    •	метод инициализации __init__ ;
    •	метод должен контролировать значения аргументов на корректность; ввод с клавиатуры read ;
    •	вывод на экран display .
Реализовать внешнюю функцию с именем make_тип() , где тип — тип реализуемой структуры.
Функция должна получать в качестве аргументов значения для полей структуры и возвращать структуру требуемого типа.
При передаче ошибочных параметров следует выводить сообщение и заканчивать работу.
В раздел программы, начинающийся после инструкции if __name__ = '__main__': добавить код,
демонстрирующий возможности разработанного класса.

1.(21) Поле first — дробное число; поле second — целое число, показатель степени.
Реализовать метод power() — возведение числа first в степень second. Метод должен правильно работать при любых
допустимых значениях first и second.
"""


class Number:
    def __init__(self, first=0.0, second=0):
        self.first = first
        self.second = second

    def read(self):
        self.first = float(input("Введите дробное число >> "))
        self.second = int(input("Введите целое число >> "))

    def display(self):
        result = self.first ** self.second
        print(f"{self.first} ^ {self.second} = {result}")


def make_power(first, second):
    # Если число возводимое в степень равно 0
    if first == 0:
        raise ValueError
    else:
        return Number(first, second)


if __name__ == "__main__":
    newNumber = Number(3, 4)
    newNumber.display()
    newNumber.read()
    newNumber.display()

    # Пример исключения
    test = make_power(0, 1.2)
    test.display()
