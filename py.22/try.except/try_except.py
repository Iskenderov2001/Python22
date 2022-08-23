# Обработка исключений
# Operator: Try...except

# Ошибки -> связанные с кодом:
# Syntax Error
# IndentationError
#    if a > 0
    # print(a)
# TypeError
# Исключение -> Invalid values
# ZeroDivisionError
# ArithmeticError
# NameError
# KeyError
# ValueError
# ImportError
# BaseException #Прородитель всех ошибок

# Try...except
# try:
#     <exprssion>
# except <Exception>:
#     <bode>
# <else>: Если всё ок
#     <body>
# <finally>: В любом случае сработает в конце.
#     <body>

# print(dir(__builtins__))

# num1 = int(input('Введите число: '))
# print(num1)
# print('Ochen\' vajnaia strochka koda! ')


# try:
#     num1 = int(input('Введите число: '))
#     print(num1)
# except:
#     print('Invalid Value, try again!')

# print

# print('Ochen\' vajnaia strochka koda! ')

# Способы увидеть ошибку
# 1. import sys

# ls = [1, 2, 3, 4, 5,]

# try:
#     index = int(input('Vvedite oshibku index: '))
#     print(ls[index])
# except:
#     import sys
#     print(f'oops, we catched {sys.exe_info() [0]} error! ')

# 2. Exception as e 

# while True:
#     try:
#         index = int(input('Vvedite oshibku index: '))
#         print(ls[index])
#     except Exception as e:
#         print(f'oops, we catched {e.__class__} error! ')


# try:
#     num1 = int(input("Введите число!: "))
#     num2 = int(input("Введите число 2: "))
#     result = num1 / num2
# except ValueError:
#     print('Вы ввели некорректные данные! ')
# except ZeroDivisionError:
#     print('Na 0 delit nelzia!!! ')
# else:
#     print('Result of division', result)
# finally:
#     print('The end')


# """
# 2) Создайте вложенный словарь, в котором ключами будут имена студентов, а значениями - другой словарь, в котором ключи - названия предметов, а значения - баллы за предмет данного студента. Далее с помощью dictionary comprehension обновите этот словарь, присвоив по 2 экстра балла каждому студенту по каждому предмету.
# Например: 

# Результат:
# {'Sam': {'math': 97, 'literature': 90}, 'Alice': {'math': 72, 'literature': 100}}
# """

# a = {'Sam': {'math': 95, 'literature': 88}, 'Alice': {'math': 70, 'literature': 98}}
# dict_ = {key: {k: v+2 for k, v in value.items()} for key, value in a.items()}
# print(dict_)

# new_dict = {
#     inner_key: x
#     for inner_key, inner_value in dict_.items()
#     for x outher_value in inner_value.items()
#     if max(inner_value.values()) == inner_value[x]
# }
# print(dict_)


# list_ = ['1','2','3']
# a = list_[0]
# b = list_[1]
# c = list_[2]
# if a == b or b == c or a == c:
#     print('yes')
# else:
#     print('ERROR')

# list_ = ['1','2','3']
# if list_[0] == list_[1] or list_[0] == list_[2] or list_[1] == list_[2]:
#     print('yes')
# else:
#     print('ERORR')
# Записать в список list_ все числа в промежутке от 54 до 9184 делящиеся на 5 без остатка.
# Распечатайте результат.
# list_ = []

# import random
# ls = []
# for x in range(0, 10):
#     ls.append(random.randint(0, 1000))
# ls.sort(reverse=False)
# print(ls)
# print(len(ls))
# for x in range(54,9184):
#     if x % 5 == 0:
#         list_.append(x)
# print(list_)

# """
# 2) Напишите программу, которая генерирует 10 случайных чисел, добавляет их в список и возвращает вам список этих чисел в отсортированном виде в порядке возрастания.
# """

# # import random
# # ls = []
# # for x in range(0, 10):
# #     ls.append(random.randint(10, 1000))
# # ls.sort(reverse=False)
# # print(ls)
# """
# 3) Напишите программу, которая заполняет список словами, введенными с клавиатуры, измеряет длину каждого слова и добавляет полученное значение в другой список. Например, список слов – ['yes', 'no', 'maybe', 'ok', 'what'], список длин – [3, 2, 5, 2, 4]. Оба списка должны выводиться на экран.
# """




# # ls = input()
# # ls1 = ls.split(',')
# # ls3 = []
# # for x in ls1:
# #     ls3.append(len(x))
# # print(ls1)
# # print(ls3)
    

# # print(ls2)



# # for x in ls:
    

# # print(ls)
# # print(len(ls))
# # print(ls1)

# # print(len(ls.count))

# """
# 1) Напишите программу, которая запрашивает с ввода семь чисел через запятую, добавляет их в список. На экран выводит первое и последнее число списка. Затем удаляет последнее число и вместо него вставляет слово “Makers”.
# Например: 
# Ввод: Введите цифры через запятую: 5, 7, 8, 1, 3, 0, 8
# Вывод: 5 8
# [5, 7, 8, 1, 3, 0, ‘Makers’]
# """
# # a = input()
# # b = []
# # b.append(a)
# # print(b)



# # a = int(input())
# # ls = (a)
# # ls.pop(-1)
# # print(f"{ls} 'Makers'" )


# """"
# Объявите переменную count, значение которой равно 0
# Из вкладки INPUT в переменную number попадает строка состоящая из числа.
# Проверьте строку в переменной number. Если строка number состоит из числа, то преобразуйте данную строку в числовой тип данных и запишите результат в count.
# Распечатайте значение count.
# """


# # count = 0
# # number = input()
# # for x in number:
    
# #     if x.isdigit():

# #         number = int(number)
# #         count = count + 1
# # print(count)

# # count = 0
# # number = input()
# # number.isdigit()
# # count = number
# # print(count)
# """
# 3) Напишите мини-игру Камень-Ножницы-Бумага. Вы играете с компьютером. Для этого используйте встроенный модуль random.

# Например:
# Ввод: Ваш выбор: Камень
# Выбор компьютера: Ножницы
# Вывод: Вы выиграли!

# Ввод: Ваш выбор: Бумага
# Выбор компьютера: Ножницы
# Вывод: Вы проиграли!
# """

# import random
# comp = random.randint(1, 4)
# comp = random.randint(1, 4)
# user = int(input)

# if user and comp == 1:
#     print("Вы выбрали КАМЕНЬ")
# if user and comp == 2:
#     print("Вы выбрали БУМАГУ")
# if user and comp == 3:
#     print("Вы выбрали НОЖНИЦУ")






# HANGMAN = (
# """
# """,

# """1-STEP
# _______
# """,
# """2-STEP
#        |
#        |
#        |
#        |
#        |     
#        |     
#        | 
# _______| 
# """,
# """3-STEP
# ________
#    |   |
#        |
#        |
#        |
#        |          
#        |
#        | 
# _______| 
# """,
# """4-STEP
#  _______
#    |   |
#    0   |
#   /X\  |
#   / \  |
#        |     
#        |     
#        |
# _______|  
# """,
# """ЖАЛЬ
#  _______
#        |
#    0   |
#   |X|  |
#   / \  |
#        |     
#        |     
#        | 
# _______|
# """
# )
# while True:
    # max_wrong = len(HANGMAN) - 1
    # words = {"KUTMAN":"\n✮✮✮✮✮✮The Best student in the group Питоновая долина...",
    #          "DANIYAL":"\n☄️☄️☄️☄️☄️☄️Fireman of the second week..." ,
    #          "MAKERS" :"\n①①①①①First bootcamp in Bishkek...",
    #          "SANZHAR":"\n👨‍💻👨‍💻👨‍💻👨‍💻The best curator on Makers ",
    #          "KASYM":"\n♔♔♔♔President of Kazahstan",
    #          "БИШКЕК":"\nStolitsa Kyrgyzstana"
    #         }
    # import random
    # key = random.choice(list(words.keys()))
    # length = "*"*len(key)
    # wrong = 0
    # used = []
    # while wrong<max_wrong and length!=key:
    #     print(">>>Вот тебе небольшая подсказка:\n",words[key])
    #     print(HANGMAN[wrong])
    #     print('''>>>Вы уже предлагали следующие буквы: ''',used)
    #     print(">>>Отгаданное вами в слове сейчас выглядит так: ",length,"\n")
    #     guess1 = input("Введите букву: ")
    #     guess = guess1.upper()
    #     while guess in used:
    #         guess = input("Введите другую букву: ")
    #         guess = guess.upper()
    #     used.append(guess)
    #     if guess in key:
    #         print("Молодец! Буква ",guess," есть в слове!")
    #         new = ""
    #         for i in range(len(key)):
    #             if guess == key[i]:
    #                 new += guess
    #             else:
    #                 new += length[i]
    #         length = new
    #     else:
    #         print("К сожалению буквы ",guess," нет в слове.")
    #         wrong += 1
    # if wrong == max_wrong:
    #     print("Вас повесили ༒ ")
    #     print(HANGMAN[wrong])
    # else:
    #     print("\n\n\nУра! У тебя получилось!")
    # print("Вы предлагали следующие буквы: ",used)
    # print("Отгаданное вами в слове выглядит так: ",length,"\n")
    
    # play_again = input("Сыграем еще? (y/n): ") 
    # if play_again.lower() != "y": 
    #     break





# print(dict_)

# dict1 = dict.values('Emil': 'Aiana','Alia','Janat','Aijamal','Bermet')

dict_ = dict.fromkeys(('Alia','Janat','Aiana','Bermet'),'Emilbek')
dict_ = {key + 'Pidor': len(key) for key, val in dict_.items()}
dict_.update({'except':'Exception'})
print(dict_)

while True:
    key = input("")
    dict_[key] += 2
    print(dict_)