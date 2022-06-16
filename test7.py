import hashlib


def Rabin_Karp(s: str, subs: str) -> str:
    assert len(s) > 0 and len(subs) > 0, 'строки не могут быть пустыми'
    assert len(s) >= len(subs), 'подстрока длиннее строки'

    len_sub = len(subs)
    h_subs = hashlib.sha1(subs.encode('utf-8')).hexdigest()

    for i in range(len(s)) - len_sub + 1:
        if h_subs == hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest():

            if s[i:i + len_sub] == subs:
                return i

    return -1


s_1 = input('введите строку: ')
s_2 = input('введите подстроку для поиска: ')

pos = Rabin_Karp(s_1, s_2)
print(f'подстрока найдена в пизиции {pos}' if pos != -1 else 'подстрока не найдена')
