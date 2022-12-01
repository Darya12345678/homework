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
 


 
#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
 
n = int(input('Ведите число: N = '))
result = 1
list = []
for i in range(1, n+1):
    result = i * result
    list.append(result)

print ('Набор произведений чисел от 1 до {} = {}' .format(n, list))
