size = int(input('Введите размер списка:'))

def fill_list(size):
    list = []

    for i in range(1, size + 1):
        list.append(int(i))
    return list

def multyply_paired_elements(list):
    new_list = []
    length_list1 = len(list) // 2
    length_list2 = len(list)

    for i in range(length_list1):
        first_element = list[i]
        last_element = list[length_list2 - 1 - i]
        multuply = first_element * last_element
        new_list.append(multuply)
    if length_list2 % 2 != 0:
        first_element = list[i + 1]
        multuply = first_element ** 2
        new_list.append(multuply)
    return new_list

list = fill_list(size)
print(list)
print(multyply_paired_elements(list))
