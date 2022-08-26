import json

FILE_PATH = 'data.json'

def get_data():
    with open(FILE_PATH)as file:
        return json.load(file)



def get_id():
    with open('id.txt', 'r') as file:
        id = int(file.read())
        id += 1
    with open ('id.txt', 'w') as file:
        file.write(str(id))

def create_product():
    data = get_data()
    product = {
        'id': get_id(),
        'title': input('Enter product name: '),
        'price': float(input('Enter price the product: '))

    }
    data.append(product)

    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)
    return 'CREATED'


def update_product():
    data = get_data()
    id = int(input('Enter ID producta:'))
    product = list(filter(lambda x: x['id'] == id, data)) 

    if not product:
        return 'No such produkt!'
    index_ = data.index(product[0])
    choice = input('Что вы хотите изменить: 1 - title,2 - price')
    if choice == '1':
        data[index_]['title'] = input()

