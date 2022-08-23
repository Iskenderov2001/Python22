##########################################################
# srez strok
# string = "Aizirek Iskenderova"
# print(string[:7])
# # Aizirek
# print(string[-11:])
##########################################################
# split 
# string = "Aizirek Iskenderova"
# print(string.split(" "))
# ['Aizirek', 'Iskenderova']
##########################################################
# join
# my_list = "Aizirek Iskenderova"
# print("$".join(my_list))
# A$i$z$i$r$e$k$ $I$s$k$e$n$d$e$r$o$v$a
##########################################################
#replace
# string = "Iskenderova Aizirek"
# print(string.replace("A", "E"))
# Iskenderova Eizirek
##########################################################


# name = input("Enter your name ")
# last_name = input("Enter your last name ")
# age = int(input("how old are you? "))
# replace1 = ("*".join(last_name))
# name1 = name.replace("i","")
# print((replace1 + name1) * age)



# name = 'Steve'
# hello = 'Hello, {}'.format(name)
# print(hello)


# name = 'Steve'
# hello = "Hello, {вот сюда почему нельзя указать переменную?}".format(name)
# print(hello)

# name = "John"
# surname = "Snow"
# print(f"{name},{surname}")

# ##########################################################
# "I love Makers Bootcamp!"
# string = input("")
# i = string.count("I")
# o = string.count("o")
# e = string.count("e")
# a = string.count("a")
# print(f"Крч бувуывуы{i+o+e+a}")

# name = input('Enter your name: ')
# seredina = len(name)//2
# print(str.swapcase(name[:seredina] + "&" + name[seredina:] + "$"))
# print(seredina)

# string = 'The quick brown fox jumps over the lazy dog'

# print(string.replace('o' , '*'))
# string = 'GAREFRE GRESGRF GREKSGF;RE'
# print(string.lower())
# string = 'Emilbek'
# result = (string.split("d"))
# string = list('Emilbek')
# print(string.)

# hashtags = "makers#bootcamp#программирование#it#курсы"
# print(hashtags.split("#"))

# name = input("Ваше имя  ")
# last_name = input("Ваша фамилия")
# age = input("ваш лет")
# city = input("город где вы живёте")
# print(f'Это человек {name} {last_name} его никто не знал до {age} года, и он всё ещё живёт в городе {city}')


# string = 'abracadabra'
# print(string.replace("a" , "K" , int[3]))


# prodoljit = 'y'
# while prodoljit == 'y':
#     num = float(input("Введите число "))
#     move = input("Выберите операцию из следующих +-*/%**// --->  ")
#     num1 = float(input("Введите ещё число "))
#     if move == "+":
#         print(num + num1)
#     elif num1 == 0:
#         print("Кто ты воин? ")
#     elif move == "*":
#         print(num * num1)
#     elif num1 == "0":
#         print(num / num1)
#     elif move == "/":
#         print(num / num1)
#     elif move == "-":
#         print(num - num1)
#     elif move == "%":
#         rint(num % num1)
#     elif move == "**":
#         print(num ** num1)
#     elif move == ":":
#         print("Знак разделение пишется вот / так в Python")
#     elif move == "//":
#         print(num // num1)
#     elif move == "=" or "$" or "#":
#         print("Вы неправильно вводите операцию для move! Пожалуйста нормально пишите что хотите с ним делать!")
#     else:
#         print("Error - Ошибка")
#     prodoljit = input(f'Нажмите "y" чтобы продолжить! ')



a = ['132', '12e', 'wqe']
a[1] = 'zaa'
print(a[1])