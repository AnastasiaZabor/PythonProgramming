# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


def read_file(path: str):
    file_to_read = open(path)
    content = file_to_read.read()
    file_to_read.close()
    return content



file1content = read_file('task5.1')
file2content = read_file('task5.2')
print(file1content)
print(file2content)
