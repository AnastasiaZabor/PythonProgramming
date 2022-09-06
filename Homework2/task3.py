k = int(input('Введите число k:'))
list = []

result = 0
i = 1
while i <= k:
    result = round((1 + 1 / i) ** 2, 2)
    list.append(result)
    i += 1

print(list)
print(sum(list))