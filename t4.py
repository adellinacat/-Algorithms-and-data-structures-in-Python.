'''Пользователь вводит две буквы.
Определить, на каких местах алфавита они стоят
 и сколько между ними находится букв.
 '''

print('Ведите прописные латинские буквы:')
l1 = input('первая: ')
l2 = input('вторая: ')

l1_num = ord(l1) - 96
l2_num = ord(l2) - 96
distance = abs(l1_num - l2_num) - 1
print(f'Буква "{l1}" {l1_num}-я в алфавите\n'
      f'Буква "{l2}" {l2_num}-я в алфавите\n'
      f'Между буквами {distance} букв(ы)')