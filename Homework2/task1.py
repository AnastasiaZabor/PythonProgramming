n = []
num = input('Введите вещественное число num:')


for i in num:
    if i.isdigit():
        n.append(int(i))
print(n)
sum = 0
list_length = len(n)
for j in range(list_length):
    sum += n[j]
print(sum)





