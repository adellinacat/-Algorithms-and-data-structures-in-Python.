import hashlib

def is_eq_str(a: str, b: str, verbose=False) -> bool:
    assert len(a) > 0, 'строки не могут быть пустыми'

    ha = hashlib.sha1(a.encode('utf-8')).hexdigest()
    hb = hashlib.sha1(b.encode('utf-8')).hexdigest()

    if verbose:
        print(f'hash 1 = {ha}\nhash 2 = {hb}')

    return ha == hb

s_1 = input('введите строку 1: ')
s_2 = input('введите строку 2: ')

print('строки одинаковые' if is_eq_str(s_1, s_2, True) else 'строки разные')


