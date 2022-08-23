# Встроенные функции

# input()
# print()
# str() etc.

# map()
# filter()
# lambda
# enumerate


# Анонимные функции - lambda(такие же функции только без названия)
# lambda функции могут принимать сколько угодно аргументов, но всегда возвращают только одно выражение

# def sum_args(a, b):
#     res = a + b
#     return res

# def sum_args1(a, b): return a + b

# print(sum_args(1, 2))
# print(sum_args1(1, 2))

# sum_args2 = lambda a, b: a + b
# print(sum_args2(1, 2))

# x = lambda a, b, c: (a * b) % c
# print(x(15, 5, 11))

# get_keys = lambda x: x.keys()
# dict_ = {1: '1', 2: '2', 3: '3', 4: '4', 5: 'Hello'}
# print(get_keys(dict_))

# get_last = lambda ls: ls[-1]
# ls = [1,2,3,4,5,6,7,8,9, 'Hello']
# print(get_last(ls))

# def myFunc(n):
#     return lambda a: a * n

# myDoubler = myFunc(2)
# myTripler = myFunc(3)

# print(myDoubler(11))
# print(myDoubler(22))
# print(myTripler(11))
# print(myTripler(22))

# dict_ = {'Sanzhar': 50000, 'John': 170000, 'Aiana': 200000, 'Sultan': 55000}
# new_dict = sorted(dict_.items(),
# key=lambda x: x[1])
# print(dict(new_dict))

# map(function, Iterable) - применяет функцию к каждому элементу из последовательности и возвращает maprobject (итератор) с результатом.

# Например, с помощью map, можно преобразовать элементы. Перевести все строки в верхний регистр.

# ls = ['one', 'two', 'three', 'dict']
# # result = map(str.upper)
# result = list(map(str.upper, ls))
# print(result)
# # for x in ls:
# #     print(x)

# names = ['John', 'Sultan', 'Aiana', 'Tirion', 'Emil']

# result = list(map(lambda x: f'Hello mr/mrs {x}', names))

# dict_ = {1: 2, 3: 4, 5: 6}

# result = dict(map(lambda x: (x[0], str(x[1])), dict_.items()))
# print(result)

# from random import choices
# from string import ascii_letters, digits, punctuation
# from itertools import repeat

# # for x in repeat('Hello', 5):
# #     print(x)

# q_pass = int(input('vvedite kolichestvo parolei: '))
# result = {
#     f(choices(ascii_letters, k=10), choices(digits, k=6), choices(punctuation, k=3))
#     for f in repeat(lambda x, y, z: ''.join(set(x+y+z)), q_pass)
#     }
# print(result)
# print(f'Quantity of passwords: {len(result)}')

#-----------------------------------------------------------------
# filter(function, Iterable) -> применяет ко всем элементам iterable функцию которую мы передали и возвращает итератор с теми объектами, для которых функция вернула True



# ls = ['one', 'two', 'list', '', '100', '1', '50', 'john99']

# res = list(filter(str.isdigit, ls)) 
# print(res)


# ls = [10, 11, 102, 213, 314, 515]

# res = list(filter(lambda x: x % 2 != 0, ls))
# print(res)


# def func(stroka):
#     if len(stroka) >= 4:
#         return True
#     return False

# x = lambda stroka: len(stroka) >= 4
# ls = ['John', 'one', 'two', 'list', 'makers', 'pyhton22', 'ono']

# res1 = list(filter(func, ls))
# res2 = list(filter(x, ls))
# print(res1, res2)



# for i, x in enumerate(ls):
#     print(f'in')

# zip(iterables) - она соединяет каждый элемент итерируемых объектов между собой в тип данных tuple и возвращает его.


# ls1 = [100,2,3]
# ls2 = [100, 200, 300]

# res = list(zip(ls1, ls2))
# print(res)


# ls1 = [1, 2, 3, 4, 5]
# ls2 = [100, 200, 300, 400, 500]
# ls3 = [10, 20, 30]
# res = list(zip(ls1, ls2, ls3))
# print(res)

# zip для создания словарей
# x = ((1, 2) (3, 5))
# a = dict(x)
# print(a)


# d_keys = ['hostname', 'location', 'vendor', 'model', 'IOS', 'IP']
# d_values = ['castle_r1', 'winter_fell', 'Starks', 'Cisco', '16.0', '10.255.0.1']

# result = dict(zip(d_keys, d_values))
# print(result)


# d_keys = ['hostname', 'location', 'vendor', 'model', 'IOS', 'IP']
# data = {
#     'r1': ['London_r1', '21 New Globe Walk', 'Cisco', '4451', '15.4', '10.255.0.1'],
#     'r2': ['London_r2', '21 New Globe Walk', 'Cisco', '4451', '15.4', '101.25.10.2'],
#     'sw1': ['London_sw1', '21 New Globe Walk', 'Cisco', '3850', '16.0', '55.251.0.101']

# }

# london_data = {}
# for k in data:
#     london_data[k] = dict(zip(d_keys, data[k]))

# print(london_data

# all() 

# dict_as_list = [['a', 1], ['b', 2], ['c', 3]]
# dictionary = dict(dict_as_list)
# print(type(dictionary))

# ls = [2, '2', 3, '4', 5 ,'45', '123']
# res = [x**2 for x in filter(lambda x: type(x) == int, ls)]
# res1 = [x**2 for x in ls if type(x) == int]
# print(res)
# print(res1)

# def func(name, last_name, age, *args, **kwargs):
#     print('Имя:' , name)
#     print('Фамилия:' , last_name)
#     print('Возраст', age)
#     if args:
#         print("Статус:", args[0])
#         print("Супруг:", kwargs)
#     else:
#         print("Статус: холост(а)")

# func('John', 'Snow', 26)
# # func('Tirion', 'lanister', 21, 'Женат', wife_name='Sansa', wife_last='Stark')

# import random

# ls = []
# def add():
#     print('ADD!')
#     name = input('Vvedite imya: ')
#     ls.append(name)

# def remove():
#     print('REMOVE!')
#     if not ls:
#         print('Увы в списке имён пусто')
#         return
#     index = input('Vvedite index: ')

#     try:
#         print(ls.pop(index))
#     except IndexError:
#         print('Нет такого индекса!')
#     except ValueError:
#         print('Вы ввели некорректный индекс!')

# for x in range(0, 10):
#     func = random.choice([add, remove])
#     func()
# print(ls)

# DECORATORS
# ФУНКЦИЯ ВЫСШЕГО ПОРЯДКА - это функция корорая в качестве аргумента принимает другую функцию4

# Декоратор - это функция которая позволяет без измениение кода 
# обернуть другую функцию для того чтобы расширит функционал обернутой функции

# def decorator(func):
#     print(func)
#     print('Я декоратор!')
#     return func()

# def hello():
#     print('Я hello!')
#     return 'Hello'

# def john():
#     print('Я John')
#     return 'John'

# print(hello())
# print()
# print(decorator(john))
# print()
# print(decorator(hello))

# def benchmark(func):
#     import time
#     start = time.time()
#     func()
#     finish = time.time()
#     print(f'Время выполнение функции {func.__name__}, заняло: {finish-start}')

# def loop():
#     i = 0
#     range_namber = 1000000
#     while i <= range_namber:
#         print(i)
#         i += 1
        
# benchmark(loop)

# Pythonic way -> @benchmark
# Синтаксический сахар - это красота кода

# def benchmark(func):
    # def wrapper():
    #         import time
    # start = time.time()
    # func()
    # finish = time.time()
    # print(f'Время выполнение функции {func.__name__}, заняло: {finish-start}')
    
    # return wrapper

    # def loop():
    # i = 0
    # range_namber = 1000000
    # while i <= range_namber:
    #     print(i)
    #     i += 1

# def strong(func):
#     def wrapper(*args, **kwargs):
#         return '<strong>' + func() + '</strong>'
#     return wrapper
    
# def div(func):
#     def wrapper(*args, **kwargs):
#         return '<div>' + func() + '</div>'
#     return wrapper

# def get():
#     return "John Snow"

# print(get())
