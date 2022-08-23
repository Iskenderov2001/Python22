# while expression:
    # <body>

# i = 1
# while i <= 10:
#     print(f'cycle {i} execute ')
#     i += 1

# name1 = 'Emilbek'
# name2 = 'Jena'
# i = 0
# while name1.lower() != 'Emilbek' or name2.lower() != 'Moia Jena':
#     name1 = input('vvedite imya1: ')
#     name2 = input('vvedite imya2: ')
#     i += 1
#     if i > 5:
#         print(print('cycle stopped'))
#         break
# else:
#     print('You entered the wrong name')

# admin = ['John', '123']
# i = 3 
# password = None

# while admin[1] != [password]:
#     password = input(f'{admin[0]} enter password\': ')
#     i -= 1
#     if i == 0:
#         print("Your account blocked ")
#         break
# else:
#     print(f'{admin[0]} you joined accaunt')


# for <variable> in <iteravle object>:
    # <body>

# list_ = [0,1,2,3,4,5,6,7,8,9]
# i = iter(list_)
# print(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# for i in list_[::-1]:
#     print(i)

# secret_list = ["DeltaViski", 'LOTR123', 'TwentyTwoRiders']
# nick = input('Enter youk user: ')

# while nick not in secret_list:
#     print("Incorrect nick! Try one momre time: ")
#     nick = input("Enter your user: ")
# else:
#     print(f'You\'re welcome my dear friend, {nick}! ')

# 6 = [3, 1, 6, 2]

#22134, 1343256, 9868534234, 4135432984
# a = 2213400000000000000
# result = [1, a]
# for i in range(2, int(a ** 0.5)+1):
#     if  a % i == 0:
#         result.extend([i, a // i])
# result.sort()
# print(result)
# print(len(result))
# # print(len(result))

# number1 = 100
# result = [1, number1]

# for i in range(2,)
# string1 = "America"
# string2 = "Japan"
# print(f'{string1[0]}{string2[0]}{string1[3]}{string2[2:]}')

# 
# string = "          Как прекрасен этот мир!   "
# a = string.strip()
# print(a)
# print(string)


# string = "      Как прекрасен этот мир!   "
# print(string.strip(), "dasdsa")
# print(len(string.strip()), sep='\n')

# string = "cow loves good milk"
# a = string.replace("o" , "e")
# print(a)

# string = "cow loves good milk"
# print(string.replace('o', 'e', 3))


# a = 1
# while a <= 10:
#     print(a ** 2)
#     a += 1
    
# a = 2
# x = 0
# while x <= 20:
#     print(a ** x)
#     x += 1

# a = 0
# while a <= 25:
#     print(2 ** a)
#     a += 1

# letters = 'ЫВыфвВЫЫвАЫВФавыаыфвцЦУуйВЫвыфЙЦАыфФ'
# a = ''
# for i in letters:
#     if i.islower():
#         a +=i
# print(a)

# 4)
# Анна решила представить некую таблицу с заглавными и строчными буквами русского алфавита в красивом формате. 
# Об этом ее попросили англоязычные друзья из социальных сетей.

# Недолго думая девушка создала скрипт, который выполнял подобную операцию. 
# Результат работы программы продемонстрирован ниже. 
# Сможете повторить (в строках с галочками - их 27 штук, чтобы вам не пришлось долго считать)? Для идентичности результатов примените любой моноширинный шрифт (в котором все символы имеют одинаковую ширину).

# Результат:
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^
# |  А а  ||  К к  ||  Х х  |
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^
# |  Б б  ||  Л л  ||  Ц ц  |
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^
# |  В в  ||  М м  ||  Ч ч  |
# ^^^^^^^^^^^^^^^^^^^^^^^^^^
# |  Г г  ||  Н н  ||  Ш ш  |
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^
# |  Д д  ||  О о  ||  Щ щ  |
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^
# |  Е е  ||  П п  ||  Ъ ъ  |
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^
# |  Ё ё  ||  Р р  ||  Ы ы  |
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^
# |  Ж ж  ||  С с  ||  Ь ь  |
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^
# |  З з  ||  Т т  ||  Э э  |
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^
# |  И и  ||  У у  ||  Ю ю  |
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^
# |  Й й  ||  Ф ф  ||  Я я  |
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^

# a = 'йцукенгшщзхъфывапролджэячсмитьбюё'
# for i in range(11):
#     print('^' * 27)
#     for letter in a:
#         if a.index(letter) % 11 == i:
#             print('|', letter.upper(), letter,' |' end='')
#     print()
# print('^' * 27)

# rus = 'йцукенгшщзхъфывапролджэячсмитьбюё'
# for i in range(11):
#     print("^" * 27)
#     for letter in rus:
#         if rus.index(letter) % 11 == i:
#             print('| ', letter.upper(), letter,' |', end='')
#     print()
# print('^' *27)


# import random

# input('Введите имя')
# select = input('Хотите поиграть? (да/нет):')

# i = 0
# while i == 0:
#     if select == 'да' or select == 'Да':
#         num = random.randint(0, 10)
#         # print(num)
#         j = 0
#         count = 0
#         while j == 0:
#             user_num = input('Введите число от 0 до 10:')
#             if user_num.isdigit():
#                 user_num = int(user_num)
#                 if num == user_num:
#                     select = input(f'Вам потребовалось {count + 1} попыток \nХотите поиграть еще раз? (да/нет):')
#                     j = 1
#                 elif num != user_num:
#                     count += 1
            
#     elif select == 'нет':
#         print('Программа закрыта')
#         i = 1
#     else:
#         print('Введите именно да или нет:')
#         select = input('Хотите поиграть? (да/нет):')




















