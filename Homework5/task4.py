def read_file(path:str):
    file_to_read = open(path)
    content = file_to_read.read()
    file_to_read.close()
    return content

def compression(content:str):
    new_str = ""
    element = content[0]
    count = 0
    for symbol in content:
        if element == symbol:
            count += 1
        else:
            new_str += f"{count}x{element} "
            count = 1
            element = symbol
    new_str += f"{count}x{element}"
    return new_str

def decompression(content:str):
    list = []
    str1 = content.split(" ")
    result = ""

    for strr in str1:
        str2 = strr.split("x")
        list.append(str2)
    for pair in list:
        for character in range(int(pair[0])):
            result += f"{pair[1]}"
    return result

def write_to_file(path:str, content:str):
    file_to_write = open(path, 'w')
    file_to_write.write(content)
    file_to_write.close()

file1 = read_file('task4.1')
print(file1)
file2 = read_file('task4.2')
print(file2)
res1 = compression(file1)
write_to_file('task4.2', res1)
# print(res)
str1 = decompression(file2)
write_to_file('task4.3', str1)
print(str1)

