import random

list = []

for i in range(1, 50, 5):
    list.append(i)
print(list)

list1 = list
print(list1)

length_list = len(list1)
for j in range(0, (length_list - 1)):
    new_index = random.randint(0, (length_list - 1))
    print(new_index)
    temp = list1[j]
    list1[j] = list1[new_index]
    list1[new_index] = temp
print(list1)

