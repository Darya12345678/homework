#Напишите 
# программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
a = int (input('Введите число, обозначающее день недели '))
if a == 6 or a == 7:
    print('день недели является выходным')
else:
    print('день недели не является выходным')   

#Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x = 1
y = 2
z = 4
a = not(x | y | z) 
b = (not x) & (not y) & (not z)
g = (a==b)
print (g)

#Напишите программу, которая принимает на вход координаты точки 
# (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка.
x = int(input ('x = '))
y = int(input ('y = '))
if (x > 0) & (y > 0):
    print ('Номер четверти плоскости - один')
elif    (x < 0) & (y > 0) :
     print ('Номер четверти плоскости - два')
elif    (x < 0) & (y < 0) :
     print ('Номер четверти плоскости - три')
elif   (x > 0) & (y < 0) :
     print ('Номер четверти плоскости - четыре')

