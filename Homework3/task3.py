#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницумежду максимальным и минимальным значением дробной части элементов.
import random

size = int(input('Введите размер списка:'))

def fill_list(size):
    list = []

    for i in range(0, size):
        list.append(round(random.uniform(1, 10), 2))
    return list

def fill_float_list(list):
    new_list = []

    for i in range(len(list)):
        num = list[i] - int(list[i])
        new_list.append(round(num, 2))
    return new_list

def max_min_decimals_difference(list):
    diff = max(list) - min(list)
    return round(diff, 2)

list = fill_list(size)
print(list)
float_list = fill_float_list(list)
print(float_list)
diff = max_min_decimals_difference(float_list)
print(diff)