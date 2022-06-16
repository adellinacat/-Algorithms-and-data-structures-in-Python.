'''Найти максимальный элемент среди минимальных элементов столбцов матрицы.
Примечание: попытайтесь решить задания без использования функций
max, min, sum, sorted и их аналогов, в том числе написанных самостоятельно.
'''

from random import random

line = 5
column = 5
a = []
for i in range(column):
    b = []
    for j in range(line):
        n = int(random() * 100)
        b.append(n)
        print('%4d' % n, end='')
    a.append(b)
    print()

mx = -1
for j in range(line):
    mn = 100
    for i in range(column):
        if a[i][j] < mn:
            mn = a[i][j]
    if mn > mx:
        mx = mn
print("Максимальное число среди минимальных: ", mx)
