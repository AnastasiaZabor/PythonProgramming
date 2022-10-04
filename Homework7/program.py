import model
import json_convert

def write_to_file(path, content):
    file = open(path, 'w')
    file.write(content)
    file.close()

def read_file(path):
    file = open(path, 'r')
    content = file.read()
    file.close()
    return content

str1 = model.Record('Sasha', 756438)
str2 = model.Record('Nastya', 125678)
new_list = [str1, str2]
dict = model.Record_dictionary(new_list)
path = 'file.json'
serialized_dict = json_convert.serialize(dict)
# write_to_file(path, serialized_dict)
data = read_file(path)
deserialized = json_convert.deserialize(data)
print(deserialized)
