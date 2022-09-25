#дз 3 задача №1
import random


def fill_list(size):
    list = [random.randint(1, 15) for i in range(0, size)]
    return list

def sum_even_indexes(list):
    indexes = [i for i in range(len(list)) if i % 2 != 0]
    filtered = [list[i] for i in indexes]
    return sum(filtered)


size = int(input('Введите размер списка:'))
list = fill_list(size)
print(list)
sum = sum_even_indexes(list)
print(sum)
