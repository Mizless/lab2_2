"""Лабораторная работа №2. Вариант 14.

Молофеев Иван. Группа ИСТбд-21.

Вычислить сумму знакопеременного ряда -(|х(3n-1)|)/(3n-1)!, где х-матрица ранга к (к и матрица задаются случайным образом),
n - номер слагаемого. Сумма считается вычисленной, если точность вычислений будет не меньше t знаков после запятой.
У алгоритма д.б. линейная сложность. Операция умножения –поэлементная."""

import random
import numpy as np


def matrix(M, matr_name):
    print("Матрица " + matr_name)
    for i in M:  # перебор всех строк матрицы
        for j in i:  # перебор всех элементов в строке
            print("%5d" % j, end=' ')
        print()


randomFill = random.randint(1, 10)
x = np.zeros((randomFill, randomFill), int)
a = np.zeros((randomFill, randomFill), dtype=float)
sum = 0
for i in range(randomFill):
    for j in range(randomFill):
        x[i][j] = np.random.randint(1, 10)
matrix(x, "x:")                            # выводим матрицу

t = int(input("\nВведите количество знаков после запятой при вычислении неточности: \n"))
t1 = 0.1 ** t

number = 1
modl = 1
factorial = 1
determinant = 0
difference = 1
ns = 0
while abs(difference) > t1:
    ns += sum
    number += 1
    temp = (3 * number) - 1
    factorial = np.math.factorial(temp)
    modl = - np.linalg.matrix_power(x, temp)
    determinant = np.linalg.det(modl)
    sum = sum + (determinant/factorial)
    difference = abs(ns - sum)                  # проверка точности вычислений
    ns = 0
    print(number - 1, ':', sum, ' ', difference)
print('Сумма знакопеременного ряда:', sum, '\nТочность:', t)