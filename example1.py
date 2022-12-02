# #Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# string = input('Введите вещественное число: ').split('.')
# a = string[1]
# b = string[0]
# a = int(a)
# b = int(b)
# n = a
# d = 1
# m = b
# y = 1
# sumleftpart = 0
# sumrightpart = 0
# while n > 0:
#     d  = n % 10
#     n = n // 10
#     sumleftpart += d
    
# while m > 0:
#     y = m % 10
#     m = m // 10
#     sumrightpart += y
    

# print(sumleftpart + sumrightpart)
 


 
# #Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
 
# n = int(input('Ведите число: N = '))

# result = 1
# list = []
# if n > 0:
#     for i in range(1, n+1):
#          result = i * result
#          list.append(result)

#     print ('Набор произведений чисел от 1 до {} = {}' .format(n, list))
# else: print('Число не может быть отрицательным и не должно быть равно нулю')


# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

# Пример:

# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06
n = int(input('Ведите число: N = '))
result = 0
list = []
summ = 0
if n > 0:
     for i in range(1, n+1):
              result = round((1 + 1/i)**i, 2)
              summ = summ + result
              list.append(result)      

     number = []
     for j in range(1,n+1):
         num = j
         number.append(num)
else : print('Число должно быть положительным и не должно быть равно нулю')

dictionary = dict(zip(number, list))
print('{}  Сумма {} '.format(dictionary,summ))

# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

# n = int(input('Ведите число: N = '))
# list = []
# result = 1
# for m in range (-n,n+1):
#     list.append(m)

# a = []
# for element in input('Введите индексы через пробел: ').split():
#      a.append(int(element))
 

# for k in (a): 
#      j = k
#      i = list[j]
#      result = i * result
       
# print('Список : {}'.format(list))
# print('Индексы элементов: {}'.format(a))
# print('Произведение элементов =  {}'.format(result))

# # Реализуйте алгоритм перемешивания списка.
# import random
# list = ['1', '2', '3', '4', '5'] 
# random.shuffle(list) 
# print(list)





    
         



