# Работа с файлами

# Каретка - Указатель - Курсор

# open(<Путь до вашего файла>)

# file = open('/Home/iskenderov/Desktop/py.22/files/files.py') #Абсолютный путь до файла.
# file = open('files.py') # Относительный путь
# print(file)

# Режимы работы с файлами

# 1. r/r+ (read)
# 2. w/w+ (write)
# 3. a/a+ (append)

# file = open('tex.txt', 'r')
# print(file)
# data = file.read()
# print(data)
# data = data.split('\n')
# print(data)
# print(type(data))

# data = file.readline()
# print(data)
# data1 = file.readline(3)
# print(data1)

# data = file.readlines()
# print(data)
# print(dir(file))

# file = open('text.txt', 'w')
# print(file)
# file.write('Hello world! \nMy names is John Snow!')
# file.close() 

# file = open('text.txt', 'w+')
# print(file)
# file.write('Hello world! \nMy names is John Snow!')
# print(file.tell())
# file.seek(1)
# print(file.read())
# file.close()

# with open('text.txt', 'r') as file:
    # data = file.read()
    # print(data)

# print(file.read())

# ls = ['Hello world', 'My name is John Snow', 'I\'m 35 years old!']
# with open('text.txt', 'w') as f:
#     f.writelines(line + '\n' for line in ls)


# from PIL import Image
# import pytesseract
# import re
# def get_imei_codes(list_images):
#     list_of_imei = []
#     for image in list_images:
#         string = pytesseract.image_to_string(image)
#         print(string)
#         list_of_imei.append(
#             re.findall(
#                 r'IME.\d.\s\d+', string)
#         )
#     with open('imeicodes.txt', 'w') as file:
#         for x in list_of_imei:
#             for i in x:
#                 file.write(f'{i}\n')


# ls = ['imei.jpg', '/home/iskenderov/Desktop/py.22/files/imei.jpg']
# get_imei_codes(ls)
