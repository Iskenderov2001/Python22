# Область видимостии пространства имён или же просто scopes определяет контекст переменной, в рамках которого мы можем её использовать.

# built-in (Встроенная) - print, len, max
# global - (Глобальная)
# enclosed - (не локальная, nonlocal)
# local (локальная область)

# main()

# def myfunc():
#     x = 300
#     print(x)

# myfunc()

# a = 10 #global
# print(a) #built-in
# def hello(): #global
#     a = 'hello world'
#     print(a, 'local inside at func')

# hello()
# print(a, 'global')

# x = 'global'
# print(x)

# def enclosed(): #global
#     x = 'enclosed'
#     def local(): #local
#         x = 'local'
#         print(x)
#     print(x)
#     local()
#     print(x)

# enclosed()
# print(x)


# LEGB
# local - enclosed - global - built-in
# len = 5
# len()
# print(len([1,2,3,4,5,6,7,8]))

# a = 10

# def func():
#     print(a)
#     a = 15
#     print(len)

# func()

# var = 100 #global variable

# def increment():
#     var += 1 #try to update a global variable inside local scope
#     print(var)

# increment()

# global -> позволяет изменять значение глобальной переменной находясь в локальной области и видимости.

# nonlocal -> позволяет изменять значение нелокальной переменной находясь в локальной области видимости.

# var = 100

# def increment():
#     global var
#     var += 1 # var = var + 1

# print(var)
# increment()
# increment()
# increment()
# increment()
# increment()
# increment()
# print(var)



# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment

# c = counter()
# print(c) # <function counter.<locals>.increment at 0x7f3737393160>

# print((c))
# print((c))
# print((c))
# print((c))
# print((c))
# c = counter()
# print(c()) # 1

# i = 0
# for x in range(0, 9999):
#     if x % 3 == 0 and x % 5 == 0:
#         i += 1
# print(i)


# print(dir(__builtins__))
# print(len(dir(__builtins__)))

# print(abs(-15)) # Стандартный вызов встроенный функции.

# abs = 15
# print(abs)
# del abs

# print(abs(-26))

# Дан список внутри которого список из трех чисел. Нужно найти максимальную сумму среди всех списков.
# [[1,2,3], [3,3,5]] -> 6, 11 -> 11

# ls = [[1,2,3], [3,3,5]]

# def find_max(ls):
#     sums = []
#     for x in ls:
#         print(sum(x))
#         sums.append(sum(x))
#     return max(sums)

# print(find_max(ls))

# res = max([sum(x) for x in ls])
# print(res)