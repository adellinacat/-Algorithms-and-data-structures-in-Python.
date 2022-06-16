h_list = [None] * 26


def my_append(value):
    index = ord(value[0]) - ord('a')
    h_list[index] = value
    print(h_list)


a = 'apricot'
my_append(a)
b = 'banana'
my_append(b)
c = 'apple'
my_append(c)


def my_index(value):
    letter = 26
    index = 0
    size = 10000

    for i, chair in enumerate(value):
        index += (ord(chair) - ord('a') + 1) *letter ** i
    return index % size

print(my_index(a))
print(my_index(b))
print(my_index(c))