
import sys

x1 = float(input('Введите координату X первой точки '))
y1 = float(input('Введите координату Y первой точки '))
x2 = float(input('Введите координату X второй точки '))
y2 = float(input('Введите координату Y второй точки '))
if x2 == x1:
    print('Error')
    exit()
k = (y2 - y1) / (x2 - x1)
b = (y1 - k * x1)
if b == 0:
    print(f'Уравнение прямой y = {k:.2f}x')
elif b > 0:
    print(f'Уравнение прямой y = {k:.2f}x + {b:.2f}')
else:
    print(f'Уравнение прямой y = {k:.2f}x - {abs(b):.2f}')

sum_ = 0
var_lst = (x1, y1, x2, y2, k, b)
for i in var_lst:
    sum_ += sys.getsizeof(var_lst)

print('*' * 30)
print(sys.version)
print(f'Под переменные задействованно {sum_} байт памяти')

#3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)]
# Под переменные задействованно 528 байт памяти
