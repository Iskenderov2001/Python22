# num = {
#     'Aiana': 22,
#     "Nurgul": 30,
#     'Sultan': 18
# }

# num1 = []
# # print(num1)
# for x in num.values():
#     x = x + 2
#     num1.append(num.keys())
# print(num1)

# list_ = [x for x in range(0, 21) if x % 2 == 0]
# print(list_)

# a = ['Alia', 'Bermet', 'Alica', 'Aiana']
# b = ['Priglashau na gorod ' + x for x in a]
# print(b)

# def welcome(name, lastname): 
#     return f"Привет {name}, по фамилии {lastname}"

# welcome("Пушкин", "Алекс")
# a = [6, 8, 9, 88, 96, 987, 24, 62]
# for x in a:
#   print(f'{max(a)} - {min(a)}')

# def aiana():
#     num1 = int(input())
#     num2 = int(input())
#     print(num1 + num2)

# aiana()

# def square(x):
#     print("Kvadrat", x,'=', (x**2))

# square(7)

# for x in range(0, 11):
#     square(x)

# def proverka(x):
#     if x % 2 == 0:
#         print(f"{x} Chetnoe")
#     else:
#         print(f'{x} Nechetnoe')

# for i in range(20, 31):
#     proverka(i)

# def factorial(n):
#     pr = 1
#     for i in range(2, n + 1):
#         pr = pr*i
#     print(pr)

# factorial(6)

# def get_string_length(string):
#     length = len(string)
#     return length
# string = input()
# print(get_string_length(string))


# dict_ = {'a': 0, 'b': 1, 'c': 2}
# def dictionary():
#     for x in dict_.keys():
#         print(x)
#         return(x)
        
        
# def function(a, b, c):
#     return((a ** 2 + b ** 2) == c**3)

# a = function(2,2,2)
# print(a)

# def piz(name, last_name):
    # return f'Welcome{name} {last_name}'

# piz('weyt', 'qweqwr')

# def union(work):
#     lists = list(work)
    
#     return lists

# print(union('Pizdez'))

# def divide(x, y):
#     res = x / y
#     print(res)
#     # return res

# divide(10500, 250)

# def devide(x, y):
#     x = devide(1500, 250)
#     y = x + 10
#     print(y)
#     return y

def divide(x, z):
    res = x / z
    y = x + 10
    print(y)
    return res

# res = devide(1500, 250)

# devide(1)

x = divide(1500, 250)
y = x + 10
print(y)

