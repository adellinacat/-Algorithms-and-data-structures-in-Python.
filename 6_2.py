'''Пользователь вводит две буквы.
Определить, на каких местах алфавита они стоят
 и сколько между ними находится букв.
 '''

import sys
import ctypes
import struct


print('Ведите прописные латинские буквы:')
l1 = input('первая: ')
l2 = input('вторая: ')

l1_num = ord(l1) - 96
l2_num = ord(l2) - 96
distance = abs(l1_num - l2_num) - 1

print('*' * 30)

print(f'Буква "{l1}" {l1_num}-я в алфавите\n'
      f'Буква "{l2}" {l2_num}-я в алфавите\n'
      f'Между буквами {distance} букв(ы)')

sum_ = 0
var_lst = (l1_num, l2_num)
for i in var_lst:
    sum_ = sys.getsizeof(var_lst)
print('*' * 30)

print(sys.version)

print(sys.getsizeof(l1_num), id(l1_num), ctypes.string_at(id(l1_num)))
print(sys.getsizeof(l2_num), id(l2_num), ctypes.string_at(id(l2_num)))

print(f'Под переменные задействованно {sum_} байт памяти')

#******************************
#3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)]
#28 2219671552240 b'\xc7'
#28 2219671552272 b'\x86'
#Под переменные задействованно 56 байт памяти