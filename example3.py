# Вычислить число c заданной точностью d

# Пример:

# - при d = 0.001, π = 3.141   
#     Ввод: 0.01
#     Вывод: 3.14

    # Ввод: 0.001
    # Вывод: 3.141

# d = float(input('Введите d: '))
# res = d
# cur = 0
# x = 1

# while x > 0:
#    r = res * 10
#    x = (1 - (res * 10))
#    cur = cur + 1
#    res = r

# import math
# a = math.pi
# n1, n2 = str(a).split('.')
# print(float(f'{n1}.{n2[:cur]}'))

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
 
# m = int(input('Введите натуральное число N: '))
# n = m
# div = 2
# list = []
# while n > 1:
#     if n % div == 0:
#         list.append(div)
#         n = n // div
#     else:
#         div += 1

# print('Список простых множителей числа {} : {} '.format(m, list))


# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]

# a = [1,1,2,3,4,4,4]
# r = []
# for i in a:
#    if a.count(i) == 1:
#      r.append(i) 

# print(r)



# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
 
# from random import randint
# k = int(input('Введите натуральную степень k:'))
# first_koef = [randint(1,100)]
# list_koeff = [randint(0,100) for i in range(k)]+ first_koef

# pol ='+'.join([f'{(j,"")[j==1]}*x^{i}' for i, j in enumerate(list_koeff) if j][::-1])                                                      
# pol=pol.replace('x^1+', 'x+')
# pol=pol.replace('x^0', '=0')
# pol = pol.replace('*=0','=0')

# print(pol)

# data = open('file.txt', 'w')
# data.writelines (pol)
# data.close()
 



      

# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов 
# (складываются числа, у которых "х" в одинаковых степенях). 
# Пример того, что будет в итоговом файле: 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0

# from random import randint
# k = int(input('Введите натуральную степень k:'))
# first_koef = [randint(1,100)]
# list_koeff = [randint(0,100) for i in range(k)]+ first_koef

# pol ='+'.join([f'{(j,"")[j==1]}*x^{i}' for i, j in enumerate(list_koeff) if j][::-1])                                                      
# pol=pol.replace('x^1+', 'x+')
# pol=pol.replace('x^0', '=0')
# pol = pol.replace('*=0','=0')

 
# y = pol
# print(y)
# data = open('file1.txt', 'w')
# data.writelines (y)
# data.close()

data = open('file.txt', 'r')
for line in data:
    text = line
data.close()



data = open('file1.txt', 'r')
for i in data:
    text1 = i
data.close()

list = text.replace('+','*')
list = list.replace('=0','*')


list1 = text1.replace('+','*')
list1 = list1.replace('=0','*')


list = list.split('*')
list1 = list1.split('*')
print(list,list1)

n = []
for i, k  in enumerate(list):
    for j in list1:
        if k == j:
            res = int(list[i - 1])+int(list1[i -1])
            result = f'{res}*{k}'
            n.append(result)

nul = ['=0']  
string = n + nul         
string = ','.join(string)    
 
 

string = string.replace(',','+')
string = string.replace('*+','')

print(string) 

data = open('file2.txt', 'w')
data.writelines(string)
data.close()