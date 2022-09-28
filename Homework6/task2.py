#ДЗ 3 задача №2

def fill_list(size):
    list = [i for i in range(1, size + 1)]
    return list

def multyply_paired_elements(list):
    new_list = []
    length_list1 = len(list) // 2
    length_list2 = len(list)

    for i in range(length_list1):
        new_list.append(list[i] * list[length_list2 - 1 - i])
    if length_list2 % 2 != 0:
        new_list.append(list[i + 1] ** 2)
    return new_list

size = int(input('Введите размер списка:'))
list = fill_list(size)
print(list)
print(multyply_paired_elements(list))