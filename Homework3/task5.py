#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
k = int(input('Введите число: '))

def fibonacci_numbers(k):
    list = [0, 1]
    for i in range(2, k + 1):
        fibonacci = list[i - 2] + list[i - 1]
        list.append(fibonacci)
    return list

def negative_fibonacci_numbers(list):
    list = list[::-1]
    new_list = []
    for i in range(len(list) - 1):
        if i % 2 == 0:
            num = -list[i]
            new_list.append(num)
        else:
            num = list[i]
            new_list.append(num)
    new_list += list[::-1]
    return new_list

list = fibonacci_numbers(k)
print(list)
new_list = negative_fibonacci_numbers(list)
print(new_list)


