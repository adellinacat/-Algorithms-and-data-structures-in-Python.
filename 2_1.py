'''Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем. После выполнения вычисления программа не
завершается, а запрашивает новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит
 неверный знак (не '0', '+', '-', '', '/'), программа должна сообщать об ошибке и снова
 запрашивать знак операции. Также она должна сообщать пользователю о невозможности деления
  на ноль, если он ввел его в качестве делителя
'''

def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    else:
        return a / b

def is_correct_operator(operator):
    return operator == '0' or operator == '+' or operator == '-' or operator == '*' or operator == '/'

def get_operator():
    return input('выберите действие: ')

def run_calculator(a=None, b=None):
    if a is None:
        a = float(input('введите первое число: '))
    if b is None:
        b = float(input('введите второе число: '))
    operator = get_operator()

    if not is_correct_operator(operator):
        print('неизвестное действие')
        run_calculator(a, b)
        return
    elif operator == '0':
        return
    elif operator == '/' and b == 0:
        print('попытка деления на ноль')
        run_calculator()
        return
    else:
        print(calculate(a, b, operator))
        run_calculator()

run_calculator()
