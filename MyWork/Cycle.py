# import json

# dict_ = {
#     'Alice': 40,
#     'age': 21,
#     'Emil': 22,
#     'book': 'Romeo Djuletta'
# }

# with open('id.json', 'w') as file:
#     json.dump(dict_, file)

# json_object = json.dumps(dict_)
# print(json_object)



# import json

# """
# Load Loads
# """

# with open('id.json') as file:
#     python_object = json.load(file)
#     print(python_object)
#     print(type(python_object))

# python_object['Alice'] = 18
# print(python_object)

# with open('id.json', 'w') as my_file:
#     json.dump(python_object, my_file)

# json_str = '{"name": "Alice", "age": 79, "books": "Chamber"}'
# python_object = json.loads(json_str)
# print(python_object)
# print(json_str)
# python_object.update({'color': 'yellow'})
# print(python_object)

# import json

# FILE_PATH = 'id.json'

# with open(FILE_PATH) as my_file:
#     dict_ = my_file
#     print(dict_)
    
def get_one_data():
    data = get_data()
    id = int(input("Enter id product" ))
    element = list(filter(lambda x: x['id'] == id, data))
    return element[0]