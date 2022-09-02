x = [0, 1]
y = [0, 1]
z = [0, 1]

for i in x:
    for j in y:
        for k in z:
            print(i, j, k)
            if (not (x or y or z)) == ((not x) and (not y) and (not z)):
                print('Выражения равны')
            else:
                print('Выражения не равны')


