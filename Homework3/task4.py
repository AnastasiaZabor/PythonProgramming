#Напишите программу, которая будет преобразовывать десятичное число в двоичное (без встроенных функций)
num = int(input('Введите число: '))

def binary_to_decimal_conversion(num):
    result = ""
    while num // 2 != 0:
        remainder = (num % 2)
        result = f"{remainder}" + result
        num //= 2
    result = f"{num}" + result
    return result

result = binary_to_decimal_conversion(num)
print(result)

