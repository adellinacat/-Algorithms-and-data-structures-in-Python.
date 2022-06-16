'''Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных
подстрок в этой строке.'''

s = input('введите строку: ')

def search_strings(s):
    n = len(s)
    my_str = set()
    for i in range(1, n):

        for j in range(n - i + 1):

            k = hash(s[j:j+i])

            if k not in my_str:
                my_str.add(k)

    return len(my_str)

print(f'исходная строка:  {s}')
print(f'количество подстрок: {search_strings(s)}')