# CRUD
# C - create
# R - retieve
# U - update
# d - delete

id = 4

data = [
    {'id': 1, 'title': 'Redmi Note 10', 'price': 250},
    {'id': 2, 'title': 'Redmi Note 9', 'price': 150},
    {'id': 3, 'title': 'Iphone 13 Pro Max', 'price': 1000}
]

def get_id():
    global id
    id += 1
    return id
    
def create_product():
    product = {
        'id': id,
        'title': input('Vvedite nazvaniye producta: '),
        'price': float(input('Vvesti price producta: '))}
    data.append(product)

def list_of_product():
    for product in data:
        print('Id of product:', product)
        print('Title:', product['title'])
        print()

def detail_retrieve():
    id_product = int(input('Vvedite id producta: '))
    try:
        product = list(filter(lambda x: x['id'] == id_product, data))[0]
    except IndexError:
        print('Takogo producta net!')
    else:
        print('Id:', product['id'])
        print('Title:', product['title'])
        print('Description:', product ['description'])
        print('Price', product['price'])
        print()

def update_product():
    id_product = int(input('Vvedite id producta: '))
    try:
        product = list(filter(
            lambda x: x['id'] == id_product, data
        ))[0]
    except IndexError:
        print('Takogo producta net!')
    else:
        index = data.index(product)
        choice = input('Chto uzmenit\'? (1-title, 2-price, 3-description): ')
        if choice == '1':
            data[index]['title'] = input('Vvedite novyu title: ')
        elif choice == '2':
            data[index]['price'] = input("Vvedite novyi price")
        elif choice == '3':
            data[index]['dexcription'] = input("Vvedite novyi description")
        else:
            print('Nekorektnyi vybor!!!')

list_of_product()
update_product()
list_of_product()