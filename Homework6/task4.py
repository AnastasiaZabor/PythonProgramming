# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# 'Мы неабв очень любим Питон иабв Джавабв'
# 'Мы очень любим Питон'

def delet_all_word_from_the_text(string1:str, string2:str):
    words = string1.split(" ")
    new_str = ""
    return " ".join([(lambda new_str: new_str + f'{word}')(new_str) for word in words if word.find(string2) == -1])

string1 = input('Введите строку: ')
string2 = input('Введите слово: ')
new_str = delet_all_word_from_the_text(string1, string2)
print(new_str)

