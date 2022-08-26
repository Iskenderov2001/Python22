# ООП(Объектно ориентированное программирование) - цель создание была связать поведение объекта с ее данными

# Класс - это описание того, какими свойствами(данными) и поведением(функции) поведение должен обладать объект() объект(экзампляр).

# Объект - это экземпляр класса с собственным состоянием этих свойств.

# Свойствами называют обычные переменные(name='John', height=185,)

# Поведение это обычные функции(def eat - метод)

#-----------------------------------------------------------------------------------

# kirk = ['James Kirk', 34, 'Capitan', 2000]
# snow = ['John Snow', 28, 'Police Officer', 1500]
# mccoy = ['Leonardo Mccoy', 30, 'Chief', 1800]

# for object in [kirk, snow, mccoy]:
#     print(f'Name: {object[0]}')
#     print(f'Age: {object[1]}')
#     print(f'Job: {object[2]}')
#     print(f'Salary: {object[3]}')

# class Human:
#     def __init__(self, name, age, job, salary):
#         self.name = name
#         self.age = age
#         self.job = job
#         self.salary = salary
    
#     def show_info(self):
#         return f'Name: {self.name} \nAge: {self.age}\nJob: {self.job}\nSalary:{self.salary}\n'

# kirk = Human('James Kirk', 34, 'Captain', 2000)
# snow = Human('John Snow', 28, 'Police officer', 1500)
# mccoy = Human('Leonardo Mccoy', 30, 'Chiev', 1800)

# print(kirk.name)
# print(snow.name)
# print(mccoy.name)

# print(kirk.show_info())
# print(snow.show_info())
# print(mccoy.show_info())

# class Dog:
#     # атрибуты класса
#     ushi = True
#     age = 0
#     def __init__(self, name, color):
#         '''
#         Инициализатор.
#         Именно здесь определяются атрибуты объекта от класса
#         '''
#         # в self хранится сам объект
#         # атрибуты объекта
#         self.name = name
#         self.color = color

# bobik = Dog('Bobik', 'brown')
# yumi = Dog('Yumi', 'white')
# aktosh = Dog('Aktosh', 'black')

# print(f'name: {bobik.name}, age: {bobik.age}, color: {bobik.color}, ushi:{bobik.ushi}')
# print(f'name: {yumi.name}, age: {yumi.age}, color: {yumi.color}, ushi:{yumi.ushi}')
# print(f'name: {aktosh.name}, age: {aktosh.age}, color: {aktosh.color}, ushi:{aktosh.ushi}')

# bobik.age = 3
# yumi.age = 1
# aktosh.age = 2
# aktosh.ushi = False

# print('After:')
# print(f'name: {bobik.name}, age: {bobik.age}, color: {bobik.color}, ushi:{bobik.ushi}')
# print(f'name: {yumi.name}, age: {yumi.age}, color: {yumi.color}, ushi:{yumi.ushi}')
# print(f'name: {aktosh.name}, age: {aktosh.age}, color: {aktosh.color}, ushi:{aktosh.ushi}')

# class Human:
#     age = 0
#     def __init__(self, name, weight, nationality):
#         self.name = name
#         self.weight = weight
#         self.nationaly = nationality
    
#     def birthday(self):
#         import random
#         print(f'\nHappy birthday, {self.name}!!!')
#         self.age += 1
#         self.weight += random.randint(3, 7)

# human1 = Human('John Snow', 3.7, 'American')
# human2 = Human('Abu-bakr', 3.1, 'Arabian')

# print(human1.name, human1.age, human1.weight, human1.nationaly)
# print(human2.name, human2.age, human2.weight, human2.nationaly)

# print('After 1 year:')

# human1.birthday()
# human2.birthday()

# print(human1.name, human1.age, human1.weight, human1.nationaly)
# print(human2.name, human2.age, human2.weight, human2.nationaly)

# print('After 5 month: ')

# human1.birthday()

# print(human1.name, human1.age, human1.weight, human1.nationaly)
# print(human2.name, human2.age, human2.weight, human2.nationaly)



class Student:
    univer = 'MIT'

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        self.books = []
        self.languages = {}
        self.knowledge = 0
        self.is_ready_to_work = False

    def add_point(self, point):
        self.knowledge += point
        if self.knowledge > 500:
            self.is_ready_to_work = True
            print(f'{self.name} is ready to work!!!')

    def read_book(self, book):
        self.books.append(book)
        self.add_point(50)
    
    def do_lab_works(self):
        self.add_point(50)
    
    def do_real_project(self):
        self.add_point(100)
    
    def learn_new_language(self, language, point):
        if not 60 < point <= 100:
            raise Exception('You point out of range!!!')
        self.languages[language] = point
        self.add_point(point)

st1 = Student('John', 'Snow')
st2 = Student('Jamie', 'Lanister')
print(st1.name)
print(st2.name)
print(f'Before study {st1.name}:', st1.books, st1.languages, st1.knowledge)
print(f'Ready to work: {st1.is_ready_to_work}')

st1.read_book('Game of Thrones')
st1.read_book('Martin Iden')
st1.read_book('Eugene Onegin')
st1.read_book('War and Peace')

st1.do_real_project()
st1.do_lab_works()
st1.do_lab_works()
st1.do_real_project()

st1.learn_new_language('Python', 100)
st1.do_real_project()
st1.learn_new_language('Js', 80)

print(f'After study {st1.name}:', st1.books, st1.languages, st1.knowledge)
print(f'Ready to work: {st1.is_ready_to_work}')

