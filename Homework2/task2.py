n = int(input('Введите число n:'))
list = []
multuply = 1

for i in range(1, n + 1):
    multuply *= i
    list.append(multuply)
print(list)
