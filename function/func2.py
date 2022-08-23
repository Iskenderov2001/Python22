# def sum_of_args(a, b, c, d): #a, b, c, d # параметры
#     return a + b + c + d

# result = sum_of_args
# print(result)
# print(type(result))
# print(result(5, 15, 21, 65))

#-------------------------------------------------------------------------------------------

# Позиционные и именнованные аргументы

# def printParams(a=None, b=None, c=None):
#     print(a, 'is stored in param a')
#     print(b, 'is stored in param b')
#     print(c, 'is stored in param c')

# printParams(b=1, c=4)

# def sum_of_args(a,b,c,d): #параметры
#     return a + b + c + d

# print(sum_of_args(5, 10, 20, 15)) #argumetns (аргументы)
# print(sum_of_args(a=5, c=20, d=15, b=10)) #Keyword arguments(наименованык аргументы)
# print(sum_of_args(10, 50, d=50, c=100))

#-------------------------------------------------------
# оператор * отвечает на распаковку

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = [*a, b]
# print(c)

# print(a)
# print(*a)

#----------------------------------------------------------------------------------------
# *args, **kwargs в функциях

# def printScores(student, *scores):
#     print(f'Student name: {student}')
#     print(scores)
#     print(type(scores))
#     for x in scores:
#         print('Score:', x)

# printScores('John', 112, 1243, 412, 341)

# def print_pet_names(owner, **pets):
#     print(f'Owner name: {owner}')
#     print(pets)
#     print(type(pets))
#     for pet, name in pets.items():
#         if type(name) is list:
#             print(f'{pet}:', *name)
#         else:
#             print(f'{pet}: {name}')
# print_pet_names('John Snow', dog='Rex', cat='Larry', fish=['Nemo', 'Dori', 'Aleks'], turtle='Leonardo')

# def get_some_data(a, b, *args, **kwargs):
#     print('параметры: a и b:', a, b)
#     print('Аргументы:', args)
#     print('Именованные аргументы:', kwargs)
#     print(args[0])
#     print(args[-1])
#     print(kwargs['name'])

# get_some_data(1,2,3,4,5, lang='Python', name='John Snow', car='BMW M8')

#-----------------------------------------------------------------------

# def add(a, b): return a + b

# def subtract(a, b): return a - b

# def multiply(a, b): return a * b

# def divide(a, b):
#     try:
#         return a / b 
#     except ZeroDivisionError:
#         return 'На ноль делить нельзя!'

# def main():
#     try:
#         num1 = float(input('Введите первое число: '))
#         num2 = float(input('Введите второе число: '))
#     except ValueError:
#         print("Vy vveli nekoerrektnoe chislo!")
#     operator = input('Vvedite operator(+,-,/,*)')

#     if operator == "+": print(f'Result: {add(num1, num2)}')
#     elif operator == "-": print(f'Result: {subtract(num1, num2)}')
#     elif operator == "*": print(f'Result: {multiply(num1, num2)}')
#     elif operator == "/": print(f'Result: {divide(num1, num2)}')
#     else: print("Nevernyi operator!")
    
#     question = input('Hotite prodoljit? Yes\no: ')
#     if question.lower() == 'yes':
#         main()
#     else:
#         print('Spasibo za ispolzovanie nashego calculatora! Bye bye! ')
        

