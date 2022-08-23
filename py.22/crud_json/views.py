# import json

# FILE_PATH = 'data.json'

# def get_data():
#     with open(FILE_PATH) as file:
#         return json.load(file)


# def get_one_data():
#     data = get_data()
#     id = int(input("Enter id product" ))
#     element = list(filter(lambda x: x['id'] == id, data))
#     return element[0]

# def post_data():
#     data = get_data()
#     data.append({
#         'id': int(input('Enter id product (1-100) ')),
#         'name': input('Enter name product: '),
#         'price': float(input('Enter pricein product '))
#     })
#     with open(FILE_PATH, 'w') as file:
#         json.dump(data, file)
#     return 'CREATED'

# def update_data():
#     data = get_data()
#     id = int(input('Enter id product '))
#     update = list(filter(lambda x: x['id'] == id, data))

#     if not update:
#         return 'Not product'
    
#     index_ = data.index(update[0])

#     print("---------------------------------------------------------")
#     print(data[index_])
#     print(data[index_]['name'])
#     print("----------------------------------------------------------")

    
#     data[index_]['name'] = input('Enter new name product' )
#     data[index_]['price'] = float(input('Enter new price' ))

#     update = list(filter(lambda x: x['id'] == id, data))
#     with open(FILE_PATH, 'w') as file:
#         json.dump(data, file)


# def delete_data():
#     data = get_data()
#     id = int(input('Enter id: '))
#     delete = list(filter(lambda x: x['id'] == id, data))
#     if not delete:
#         return 'Not have product!'
#     index_ = data.index(delete[0])
#     data.pop(index_)
#     json.dump(data, open(FILE_PATH, 'w'))
#     return 'DELETED'


# def func(a, b):
#     23, 41
# func()
