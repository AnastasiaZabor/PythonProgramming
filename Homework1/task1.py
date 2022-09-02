num = (int(input('Введите цифру дня недели: ')))

if (num >= 1) and (num <= 5):
    print('нет')
elif (num == 6) or (num == 7):
    print('да')
else:
    print('некорректная цифра')