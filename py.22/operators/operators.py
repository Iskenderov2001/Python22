# Операторы сравнение
# Условные операторы
# Логические операторы


# Операторы сравнение
#<, >, ==(RAVNO), <=, >=, !=(НЕ РАВНО)

# num1 = 18
# num2 = 15
# print(18 < 15)

# stroka1 = "Hello"
# stroka2 = "World"
# print(stroka1>stroka2)
# print(ord("H"))
# print(ord("W"))
# text = "Helloold"
# for letter in text:
#     print(ord(letter))

# print(chr(1080))

# if - если
# elif - иначе
# else - если

# if <condition>:
#     <body if>
#     <body if> #сработает если в if придет True

# elif <condition>:
#     <body elif>
# else:
#     <body> #сработает если во всех условиях пришло False

# string = input("Enter smt: ")
# if string == "Hello":
#     print("Hello stranger! ")
# elif string == "John": 
#     print("Welcome back John Snow! ")
# elif string == "Mercedes":
#     print("Mercedez-Benz S class! ")
# else:
#     print("Совпадение не найдено! ")
# print("Код закончился! ")

# email = input('Enter email: ')
# password1 = input('Enter password: ')
# if len(password1) < 8:
#     raise Exception('Too short password!')
# password2 = input('Enter password confirmation: ')

# if password1 != password2:
#     raise Exception('Password didn\' match')
# else:
#     print("Succesfully signed Up!")

# age = input("Возраст ваш: ")
# if age.isdigit():
#     age = int(age)
# else:
#     raise ValueError("Enter correct values! :")

# if age < 18:
#     print(f'Chuvak prihodi cherez {18 - age} let!!!')

# else:
#     print('Vy prohodite po vozrastu! ')

# password = input('Enter your password: ')
# symbols = ['_', ',', '.', '%', '#', '@', '+', '-', '*', '(', ')']

# flag = False
# for element in symbols:
#     if element in password:
#         flag = True
# if(password.isalpha()): 
#     raise Exception('Вы ввели только буквы, нужны ещё цифры! ')
# elif password.isdigit():
#     raise Exception('Вы ввели только цифры, нужны ещё буквы! ')
# elif not flag:
#     raise Exception('Вы не ввели хотя бы один спец-символ в пароль!!! (_,()...)')
# else:
#     print('Все окей вы ввели корректный пароль! ')

# else:
#     print('Всё окей!')    
# print("Все окей!")

# str1 = 'asd('
# for element in symbols:
#     print(element in str1) 
# password = input("Введите пароль! ")
# if(password.isdigit()):
#     raise Exception("вы ввели только цифру")

# name = input("Enter your name ")
# last_name = input("Enter your last name ")
# print('Hello mr/mrs %s %s' %(name, last_name))

# name = 'Stevdfwfwaee'
# hello = 'Hello'
# print(f"{name}")
# Hello, Steve 

# print('Hello, %s' % 'Vasya')

# Логические операторы
# and -> логическое и
# or -> лог или
# not -> лог отрицание
# Операторы идентификации
# in -> проверяет наличие элемента внутри какого либо массива или строки
# is -> это оператор сравнивает ячейки памяти двух элементов
# == ->  сравнивает по значение
# is not -> отрицательное сравнение ячеек памяти



# my_age = 20
# your_age = 18
# result = my_age == 20 and your_age == 18
# print(result)
# result = my_age < 18 or your_age < 17
# print(result)
# result = not my_age > 25
# print(result)

# is_google_user = True
# is_github_user = True
# is_age_greater_21 = False
# user_coins = 800

# if (is_google_user and is_github_user) and (is_age_greater_21 or user_coins > 5000):
#     print('You can enter the system mr John Snow! ')
# else:
#     print('Sorry, you couldn\t enter! ')

# str1 = 'Hello world! '
# choice = input('Введите символ ')

# if choice in str1:
#     print(f'Символ {choice} есть в строке: "{str1}" ')
# else:
#     print(f'Символа {choice} нет в строке: "{str1}" ')

# dano [1--100]
# \3 -> 3 - fu
# \5 -> 5 - ba
# \3, \5 -> 15 - fuba

# for number in range(1,100):
#     # print(number)
#     if number % 3 == 0 and number % 3 == 0:
#         print(f"{number} - fuba")
#     elif number % 5 == 0:
#         print(f"{number} - ba")
#     elif number % 7 == 0:
#         print(f"{number} - fu")

# num = 1
# while num >= 0:
#     num = int(input("В число "))
#     if num < 0:
#         print('Встретилось отрицательное число')

##############################################################################

# num = 1
# while num <= 0:
#     num = (input("Число"))
#     if num > 0:
#         print('Встертилось число')

#################################################################################

# for i in range(1, 999):
#     if i % 1 == 0 and i // 9 == int:
#        print(i)


# """
#   По теме: Логические и условные Операторы
# """
# """
# 1) Создайте программу, которая будет требовать пароль и проверять, содержатся ли в нем только числа, при этом длина пароля не должна быть менее 8 символов . Если все эти условия выполняются, то программа выдает вам сообщение ‘Ваш пароль сохранен’, если же нет - то программа должна указать необходимое условие для сохранения вашего пароля.

# Например:
# Ввод: Введите пароль: Makers12345
# Вывод: Ваш пароль должен хранить только числа

# Ввод: Введите пароль: a12345
# Вывод: Ваш пароль должен содержать не менее 8 символов
# Ваш пароль должен содержать только буквы
# # """
# # a = input("")
# # symbols = "aaaaaaaa"
# # if len(a) <= len(symbols):
# #     print("Длина пароля не должна быть менее 8 символов")
# # elif (a) == (a.isdigit):
# #     print("Добавьте буквы")
# # elif len(a) > len(symbols):
# #     print("Длина пароля достаточно")

# # a = (input())
# # operasia = "+ - / * ** // %"
# # b = float(input)

# import string
# flag = True
# simbols = string.digits + '-' + '.'
# # print(simbols)
# # print(type(simbols))
# while flag:
#     is_correct_nums = True
#     num1 = input('Vvedite pervoe chislo: ')
#     for x in num1:
#         if x not in simbols:
#             print('Вы ввели некорректное число!')
#             is_correct_nums = False
#             break
#     if not is_correct_nums:
#         continue

#     num2 = input('Vvedite vtoroe chislo: ')
#     for x in num2:
#         if x not in simbols:
#             print('Вы ввели некорректное число!')
#             is_correct_nums = False
#             break
#     if not is_correct_nums:
#         continue

#     num1 = float(num1) if '.' in num1 else int(num1)
#     num2 = float(num2) if '.' in num2 else int(num2)
#     oper = input("Введите оператор( +, - , / , * ): ")
#     if oper == '+': print(num1 + num2)
#     elif oper == "*": print(num1 * num2)
#     elif oper == "-": print(num1 - num2)
#     elif oper == "/":
#         if num2 == 0:
#             print("Нельзя делить на 0! ")
#         else:    
#             print(num1 / num2)
#     else:
#         print("Неправильный оператор!!! ")
#     choice = input("Хотите продолжить(yes/no): ")
#     if choice.lower() == "no":
#         flag = False

# a = input("")
# # b = "," .join(a)
# result = a
# print(list(result))
# b = result.split('')
# print(list(b))




# import random
# ls = []
# for x in range(0, 200):
#     ls.append(random.randint(0, 100))
# ls.sort(reverse=False)
# print(ls)
# print(len(ls))

# import random
# i = []
# for x in range(10):
#     i.append(random.randint(0, 100))
#     i.sort(reverse=False)
# print(i)
    # print(len(i))

##########################################################################################
#     import random
# i = []
# for x in range(1, 10):
#     i.append(random.randint(0, 1000))
#     i.sort(reverse=True)
#     print(i)
#     print(len(i))
#####################################################################################
# писать код здесь
# a = input(list())
# b = (',').join(a)
# c = "'Makers'"
# print(b + c)

#     import random 
# i = input()
# for x in range(1, 999):
#     i(random.randint (0, 1000))
#     i.sort(reverse=True)
#     print(i)
