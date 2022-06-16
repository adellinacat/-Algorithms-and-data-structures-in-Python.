from collections import namedtuple
from statistics import mean

New_Company = namedtuple('New_Company', 'name profit_list avg')

lst = []
for i in range(int(input('Введите количество фирм: '))):
    arg = input('Введите в строку название фирмы и поквартальную прибыль через пробел:\n').split()
    lst.append(New_Company(arg[0], arg[1:], mean(map(int, arg[1:3]))))

avg = mean([i.avg for i in lst])

for i in lst:
    print(f'Компания: {i.name} \t\tСредняя прибыль за год: {i.avg}')

print('_' * 70, '\n')

print('Компании с прибылью меньше средней: ')
for i in lst:
    if i.avg < avg:
        print(i.name)

print('Компании с прибылью больше средней: ')
for i in lst:
    if i.avg > avg:
        print(i.name)