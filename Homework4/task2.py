# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

def find_factors(n:int):
    list = []
    divider = 2

    while divider <= n:
        if n % divider == 0:
            list.append(divider)
            n //= divider
        else:
            divider += 1
        if n == 1:
            break

    return list

n = int(input("Введите натуральное число N: "))
list = find_factors(n)
print(list)



