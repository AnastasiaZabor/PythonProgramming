# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]
import random


def fill_list(size:int):
    list = []

    for item in range(0, size):
        num = random.randint(0,15)
        list.append(num)
    return list

def non_repeating_elements(list:list):
    dictionary ={}
    new_list = []

    for number in list:
        if number not in dictionary:
            dictionary[number] = True
        else:
            dictionary[number] = False

    for key in dictionary.keys():
        if dictionary[key]:
            new_list.append(key)
    return new_list

size = int(input('Введите размер списка: '))
list = fill_list(size)
print(list)
new_list = non_repeating_elements(list)
print(new_list)
