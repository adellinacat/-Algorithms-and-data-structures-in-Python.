k = int(input('введите количество предприятий: '))
enterprises = {}

for i in range(1, k + 1)
    name=input('введите название предприятия: ')
    enterprises[name]=[float(input('План: ')), float(input('Фактический: '))]
    enterprises[name].append(enterprises[name][1]/enterprises[name][0])
print('Фактическая прибыль больше 10, но план не выполнен (меньше 100%)')
for key, value in enterprises.items():
    if value[1]> 10 and value[2]<1:
        print(f'Предприятие {key} заработало {value[1]}, что составило {value[2]*100:.2f}%')