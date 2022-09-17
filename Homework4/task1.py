# Вычислить число c заданной точностью d
# Пример:
#
#     при $d = 0.001, π = 3.141
import math

def find_decimal_places(d:float):
    a = d.split(".")
    length_str = len(a[1])
    return length_str

def pi_number(d:int):
    numbers = find_decimal_places(d)
    return round(math.pi, numbers)

d = input('Введите точность числа пи:')
number_pi = pi_number(d)
print(number_pi)

