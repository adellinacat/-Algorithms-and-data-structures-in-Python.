'''Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.'''
import sys
import ctypes
import struct

bit_and = 5 & 6
bit_or = 5 | 6
bit_xor = 5 ^ 6

print(sys.version)

print(sys.getsizeof(bit_and), id(bit_and), ctypes.string_at(id(bit_and)))
print(sys.getsizeof(bit_or), id(bit_or), ctypes.string_at(id(bit_or)))
print(sys.getsizeof(bit_xor), id(bit_xor), ctypes.string_at(id(bit_xor)))

print('*' * 30)

print(f'Выполним логические побитовые операции над числами 5 и 6:\n'
      f'5 & 6 = {bit_and}\n'
      f'5 | 6 = {bit_or}\n'
      f'5 ^ 6 = {bit_xor}')

print(f'Выполним побитовый сдвиг вправо и влево на два знака с числом 5:\n'
      f'5 >> 2 = {5 >> 2}\n'
      f'5 << 2 = {5 << 2}')

# Оценка размера переменных:
#3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)]
#28 3000471191888 b'@'
#28 3000471191984 b'\x0c'
#28 3000471191856 b'\x1f'