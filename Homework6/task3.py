#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницумежду максимальным и минимальным значением дробной части элементов.
import random

def fill_list(size):
    return [round(random.uniform(1, 10), 2) for i in range(0, size)]

def fill_float_list(list1):
    return list(map(lambda num: round(num - int(num), 2), list1))

def max_min_decimals_difference(list1):
    return round((max(list1) - min(list1)), 2)

size = int(input('Введите размер списка:'))
list1 = fill_list(size)
print(list1)
float_list = fill_float_list(list1)
print(float_list)
diff = max_min_decimals_difference(float_list)
print(diff)