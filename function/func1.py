# Функция - это именнованая часть программы, которая может вызываться в других частях программы столько раз, сколько угодно.

# def name_of_function>(<a, b>)
#     <body> # код, какая то логика которая возвращает конечный результат.
#     return # оператор для возвращения результат

# name_of_function(5, 6 аргументы)

# Параметры фунции - переменные которые будет принимать наша функция, для того чтобы мы могли работать с данными которые передаются в нашу функцию

# Аргументы - данные которык мы передаём для параметров при вызове функции.

# return - оператор который нужен для того чтобы функция возвращала резцльтат, если return не указать то фукция ничего не возврщает None

# a = print("Hello")

# print(a)

# a = max(range(1, 100))
# print(a)

# def our_len(a): # параметр
#     i = 0
#     for i in a:
#         i += 1
#     return i

# ls = [1,2,3,4,5]
# str1 = "Hello world s vami John Snow!"
# our_len(ls) # argument
# print(our_len(str1))

# def  sumTwoNums(num1, num2): #параметры
#     result = num1 + num2
#     print(result)
#     return result

# a = sumTwoNums(5, 15) #arguments
# print(a)

# def isEven(num):
#     if num % 2 == 0:
#         return True
#     print("Hello!!! ")
#     return False
#     print('Hello')

# a = 10
# b = int(input('Vvedite chislo: '))
# print(isEven(9))
# print(isEven(a))
# print(isEven(b))

# def isEven1(num: int) -> bool:
#     '''Our function returns True or False
#     while checking number for even number '''
#     if num % 2 == 0:
#         return True
#     return False

# print(isEven1(90))

# dir

# from typing import List
# def get_polindrom(words: List[str]) -> List [str]:

#     """Function return a polndrom string list"""

#     result = []
#     for x in words:
#         if x.lower() == x[::-1].lower():
#             result.append(x)
#         return result

# some_words = ['John', 'Ono', 'Kazak', 'anna', 'Dovod', 'apa', 'Juice', 'peter', 'piko', 'tenet']
# print(get_polindrom(some_words))
# print(get_polindrom['John', 'Ono', 'Kazak', 'anna', 'Dovod', 'apa', 'Juice', 'peter', 'piko', 'tenet'])


# def get_percentage(money: float, period: int) -> float:
#     """Return finalamout of money"""

#     if money <30000:
#         raise Exception('Vy vveli nekorektnoe kolichecstvo deneg! min stavka 30 000 somov! ')
#     if period < 3:
#         raise Exception('Vy vveli nekorektnyi srok dlya depozita! min srok 3 goda!')

#     i = 0
#     while i < period:
#         money += money * 0.1
#         i += 1
#     return money
# money = float(input("Vvedite summu deneg: "))
# year = int(input("Vvedite srok vashego deposta: "))
# print(get_percentage(money, year))

#------------------------------------------------------------

# default = params
# def func():
    # print('Hello world!')

# func()

# def wc(name= input()):
#     print(f'Welcome, {name}! Dolban')

# wc()

# print_welcome('John')

# def introduce(name, last_name, work=None):
#     print(f'This persons name is {name}')
#     print(f'This persons last_name is {last_name}')
#     if work == 'None':
#         print(f'This persons work is {work}')
#     else:
#         print(f'This person fucking {work}')

# introduce("John", "Snow", 'None')

# 'Hello world! My nadisad feewwefwe few f ef,fewf fe f, fewf.'

# def ls(mal):
    # print(mal)


# ls = 'Hello world! My nadisad feewwefwe few f ef,fewf fe f, fewf.'
# print(ls)

# def slojenie():
#     print('Podgotovka slojenie')

# slojenie()