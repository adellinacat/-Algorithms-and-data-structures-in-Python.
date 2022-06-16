'''Определить, какое число в массиве встречается чаще всего.'''

from random import random

x = 20
arr = [0] * x
for i in range(x):
    arr[i] = int(random() * 20)
print(arr)

num = arr[0]
max_number = 1
for i in range(x - 1):
    number = 1
    for k in range(i + 1, x):
        if arr[i] == arr[k]:
            number += 1
    if number > max_number:
        max_number = number
        num = arr[i]

if max_number > 1:
    print(max_number, 'раз(а) встречается число', num)
else:
    print('Все элементы уникальны')
