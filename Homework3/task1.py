import random

size = int(input('Введите размер списка:'))


def fill_list(size):
    list = []

    for i in range(0, size):
        num = random.randint(1, 15)
        list.append(num)
    return list

def sum_even_indexes(list):
    sum = 0
    for i in range(len(list)):
        if i % 2 != 0:
            sum += list[i]
    return sum

list = fill_list(size)
print(list)
print(sum_even_indexes(list))



