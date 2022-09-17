# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
#
#     k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random


def form_a_polynomial(k:int):
    result = ""
    for i in range(k):
        member = random.randint(0, 100)
        result += f"{member}*x^{k-i}"
        if (i != k - 1):
            result += " + "
    zero_member = random.randint(0, 100)
    if zero_member != 0:
        result += f" + {zero_member}"
    result += " = 0"
    return result

def write_to_file(result:str):
    path = 'task4'
    file = open(path, 'w')
    file.write(res)
    file.close()

k = int(input("Введите натуральную степень k: "))
res = form_a_polynomial(k)
print(res)
write_to_file(res)
