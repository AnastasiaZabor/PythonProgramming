n = int(input('Введите число n:'))
list = []

for i in range(-n, n +1):
    list.append(i)
print(list)

positions = input('Введите позиции через пробел:').split()
multuply = 1

for j in positions:
    position = int(j)
    print(list[position])
    multuply *= list[position]
print(multuply)

