# strings = ['abcd', 'asdre5', 'esdg7', '777543']
# number = input()
# found = False
#
# for str in strings:
#     if str.find(number) != -1:
#         print(str)
#         found = True
# if not found:
#     print('Строки нет')

strList = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
strToFind = input()
counter = 0
index = 0

for strIng in strList:
    if strIng.find(strToFind) != -1:
        counter += 1
    if counter == 2:
        print(index)
    index += 1


