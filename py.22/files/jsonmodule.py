# javascript object notation - JSON
# Единый формат хранения и передачи данных между компютерами, сервисами, приложениями и языками программирования через сеть Интернет.
# <filename>.json

# {
#     "id": 1,
#     "author": "John",
#     "posts": Null
# } # It's JSON, mission teaching translate JSON in Python Dict

# !!!
# JS object == {}, Pyhton dict == {}, JSON == {}

# Процессы Сериализации и Десириализации данных

# Сериализация(Запись данных в JSON) - это перевод Python Dict в JSON формат.

# dump - метод записывает объект Pyhton в файл в формате JSON
# dumps - метод записывает объект Pyhton в строку в формате JSON

# Десериализация(Чтение данных из JSON) - это процесс перевода из JSON в Pyhton Dict
# load - метод который считывает файл в формате JSON и переводит его в объекты Pyhton
# loads - метод который считывает текст в формате JSON и переводит его в объекты Pyhton

#---------------------------------------------------------------------------------------------------
# Процесс десериализация
# import json
# from urllib.request import urlopen

# data = urlopen("https://randomuser.me/api")
# # print(type(data))
# # print(data)

# py_dict = json.load(data)
# print(py_dict)
# print(type(py_dict))

#---------------------------------------------------------------------------------------------------

# import json
# 
# with open('dowAPI.json', 'r') as file:
    # data = file.read()
    # print(data)
    # print(type(data))
    # user = json.loads(data)
    # print(user)

#---------------------------------------------------------------------------------------------------

import json

# dict_ = {
    # 'name': 'John',
    # 'last_name': 'Snow',
    # 'status': True,
    # 'wife': False,
    # 'children': None
# }

# string = json.dumps(dict_)
# print(string)
# print(type(string))

# with open('new.json', 'w') as file:
#     json.dump(dict_, file)