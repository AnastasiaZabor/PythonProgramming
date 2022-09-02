num = (int(input('Введите номер четверти:')))

if num == 1:
    print('x > 0, y > 0')
elif num == 2:
    print('x < 0, y > 0')
elif num == 3:
    print('x < 0, y < 0')
elif num == 4:
    print('x > 0, y < 0')
else:
    print('Такой четверти нет')