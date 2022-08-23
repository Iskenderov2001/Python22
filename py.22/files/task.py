####################################################################################################

# Имеется файл file.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту:

# количество букв латинского алфавита;
# число слов;
# число строк.

# INUT file.txt:
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.

# OUTPUT
# 108 letters
# 20 words
# 4 lines

# file = open('file.txt', 'r')

# data = file.read(10)
# file1 = []
# for x in file:
#     file1.append(x)
#     print(x)
# print(file.readline())
#--------------------------------------------------------------------------------
# slov = {'Буква': 0}
# slova = {'slova': 0}
# total_cifr = []
# text = []

# file = open('file.txt', 'r')
# list_ = file.readlines()
# esh = ''.join(list_)
# dict_ = esh.split()
# print(dict_)


# for dict1 in dict_:
#     if dict1.isalpha():
#         slova['slova'] += 1
#     elif dict1[-1] == '.':
#         slova['slova'] += 1

# for line in list_:
#     total_cifr.append(len(line))
#     text.append(line)

# for x in esh:
#     if x.isalpha():
#         slov['Буква'] += 1

# print(f' {slova["slova"]} Слов')
# print(f' {len(total_cifr)} Строк')
# print(f' {sum(total_cifr)} Символ')
# print(f' {total_cifr} Количество символ в строках')
# print(f' {slov["Буква"]} Буква')



#----------------------------------------------------------------------------
# slov = {'Цифра': 0}
# string = ("fdsfds fdfs myuim f578578 hy287 dsfdn uyjyusf fdsfdsf ")

# for alp in string:
#     if alp.isalpha():
#         slov['Цифра'] += 1
# print(f'Слов {slov["Цифра"]}')
#--------------------------------------------------------------------------------------




# print(len(file.readlines()))
# print(total_cifr.count['\n'])

# """
# 1) Создайте файл numbers.txt и напишите скрипт, который запишет в этот файл числа от 1 до 20. Затем создайте файл squares.txt. Напишите скрипт, который будет считывать числа из файла numbers.txt и записывать квадраты этих чисел в файл squares.txt
# """
# # писать код здесь






# functionNum()


# """
# 2) Создайте файл usernames.txt. Напишите скрипт, который будет запрашивать у пользователя имена, а эти имена будут помещаться в файл usernames.txt. При этом напротив каждого имени будет записано количество букв в юзернейме. Программа запрашивает имена до тех пор, пока пользователь не введёт слово: End.
# """


# fil = open('proverka.txt','r')
# # fil.readline(1)
# print(f'{len(fil.readline())}')t','r')
# fil.readline(1)
# print(f'{len(fil.readline())}')

# print(fil.readline())
# print(fil.readline())
# print(fil.readline())

# print(f'{len(fil.readline())}')
# print(f.readlines(3))

# fil.close()

# file = open('numbers.txt', 'r')

# lines = file.readlines(13)
# for line in lines:
#     print(line)

# file.close()

# with open('task2.txt','r'):
#     for x in open('task2.txt'):
#         print(x.strip())

# for x in open('task.txt'):
#     print(x.strip)

# with open("task2.txt") as bar:
    # for line in bar:

# with open('task2.txt')as f:
#     for x in f.readlines():
#         print(x.strip())

# with open('task2.txt') as f:
#     print(f.read())


# slov = 0

# with open('proverka.txt','r') as pro:
#     print(len(pro.readlines()))
#     pro.seek(0, 0)
#     print(len(pro.read()))



# OUTPUT
# 108 letters
# 20 words
# 4 lines
# with open('task2.txt') as f:
#     print(f.read())

# with open('task3.txt','w+') as f:
#     f.write('0*1*2*3*4*5*6*7*8*9*')
#     f.seek(0, 0)
#     print(f.read())

# with open('task4.txt', 'r') as f:
#     print(len(f.readlines()))

# a = []

# with open('task5.txt', 'r') as f:
#     for x in f.read:
#         print(x)

"""
1) Создайте файл numbers.txt и напишите скрипт, который запишет в этот файл числа от 1 до 20. Затем создайте файл squares.txt. Напишите скрипт, который будет считывать числа из файла numbers.txt и записывать квадраты этих чисел в файл squares.txt
"""



# with open('numbers.txt','w+') as test1:
#     test1.write(int(range(0, 21)))


# with open('numbers.txt', 'w+') as test:
#     test.write(range(0,12))


# file = open('numbers.txt', 'w')
# a = []
# for x in range(0, 21):
#     file.write(f'{str(x)}\n')
# file.close()

with open('squares.txt', 'w+') as test:
    for x in range(0, 21):
        test.write(f'{str(x)} {x**2}\n')



"""
2) Создайте файл usernames.txt. Напишите скрипт, который будет запрашивать у пользователя имена, а эти имена будут помещаться в файл usernames.txt. При этом напротив каждого имени будет записано количество букв в юзернейме. Программа запрашивает имена до тех пор, пока пользователь не введёт слово: End.
"""

# with open('usernames.txt', 'w') as test:
#     while True:
#         a = input("username ")

#         if a != 'End':
#             test.write(f'{a}\n')
#             continue
        
#         elif a == 'End':
#             test.seek(0, 0)
#             # for x in test.readlines():
#             print(f'{len(test.readlines)} ')
            
#             break

    

# a = 0

# while a < 50:
#     print(a**2)
#     a += 1

