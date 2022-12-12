"""
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
Результат округлить до сотых.
Ввод: четыре значения типа <int>
Вывод: значение типа <float>
Пример:
4 10
11 5
9.22
"""

import math

x1 = int(input("Введите координату x1: "))
y1 = int(input("Введите координату y1: "))
x2 = int(input("Введите координату x2: "))
y2 = int(input("Введите координату y2: "))

distance = float(round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 2))
print(distance)