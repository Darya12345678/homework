# #Напишите 
# # программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# a = int (input('Введите число, обозначающее день недели '))
# if a == 6 or a == 7:
#     print('день недели является выходным')
# else:
#     print('день недели не является выходным')   

# #Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# for x in [True,False]:
#     for y in [True,False]:
#         for z in [True,False]:
#          print ('not',(x, 'or', y ,'or',z) ,'=', (not x) & (not y) & (not z))
            

# #Напишите программу, которая принимает на вход координаты точки 
# # (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка.
# x = int(input ('x = '))
# y = int(input ('y = '))
# if (x > 0) & (y > 0):
#     print ('Номер четверти плоскости - один')
# elif    (x < 0) & (y > 0) :
#      print ('Номер четверти плоскости - два')
# elif    (x < 0) & (y < 0) :
#      print ('Номер четверти плоскости - три')
# elif   (x > 0) & (y < 0) :
#      print ('Номер четверти плоскости - четыре')

#     #  Напишите программу, которая по заданному номеру четверти, 
#     #  показывает диапазон возможных координат точек в этой четверти (x и y).
# a = int (input('Введите номер четверти: '))
# if a == 1 :
#     print ('диапазон возможных координат точек в этой четверти -  от 0 < X < + ထ ; 0 < Y < + ထ')
# if a == 2:
#     print ('диапазон возможных координат точек в этой четверти - от - ထ < X < 0; 0 < Y < + ထ')
# if a == 3:
#     print ('диапазон возможных координат точек в этой четверти - от - ထ < X < 0; - ထ < Y < 0')
# if a == 4:
#     print ('диапазон возможных координат точек в этой четверти - от 0 < X < + ထ ;  - ထ < Y < 0')

# # Напишите программу, которая принимает на вход координаты двух точек и
# #  находит расстояние между ними в 2D пространстве.
# a = int(input ('Введите коррдинату X первой точки '))
# b = int(input ('Введите координату Y первой точки '))
# c = int(input ('Введите координату X второй точки '))
# d = int(input ('Введите координату Y второй точки '))
# s = ((c - a)**2 + (d - b)**2)**(1./2)
# r = round(s,2)
# print(r)
p = 'file3.txt'
my_text =[]
data = open( p,'r')
for line in data:
    print(line)
    
str=line
data.close()
def del_some_words(str):
    str = list(filter(lambda x: 'abv' not in x, str.split()))
    return " ".join(str)

str = del_some_words(str)
print(str)


# 42. Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
    # - входные и выходные данные хранятся в отдельных файлах


# with open('42_RLE1_decoded.txt', 'r') as data:
#     my_text = data.read()

# def encode_rle(ss):
#     str_code = ''
#     prev_char = ''
#     count = 1
#     for char in ss:
#         if char != prev_char:
#             if prev_char:
#                 str_code += str(count) + prev_char
#             count = 1
#             prev_char = char
#         else:
#             count += 1
#     return str_code

            
# str_code = encode_rle(my_text)
# print(str_code)

# with open('42_RLE2_encoded.txt', 'r') as data:
#     my_text2 = data.read()

# def decoding_rle(ss:str):
#     count = ''
#     str_decode = ''
#     for char in ss:
#         if char.isdigit():
#             count += char 
#         else:
#             str_decode += char * int(count)
#             count = ''
#     return str_decode

# str_decode = decoding_rle(my_text2)
# print(str_decode)