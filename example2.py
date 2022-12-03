# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.

list = [2, 3, 7, 6, 8]
a = list[1::2]
print ('На нечетных индексах элементы ',a)
sum = 0
for i in (a):
    sum += i

print('Сумма элементов на нечетных индексах =', sum )

# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

num = [1, 2, 7, 5, 6]
rev_num = num[::-1]

if len(num) % 2 == 0:
     num_pairs = (len(num)) // 2
else:
     num_pairs = ((len(num)) + 1) // 2

result = []
for j in range (num_pairs) :
      res = num[j] * rev_num[j]
      result.append(res)

print('Произведение пар чисел:', result)

# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

n = [0.1, 5.3, 3.1, 3.01]
fract_n = []
for k in (n):
     element = k
     if element > 1:
         x = int(element)
         y = element - x
         d = round(y,5)
     else: d = element
     fract_n.append(d)
print(fract_n)

max_fract_n = max(fract_n)
min_fract_n = min(fract_n)

print('Разница между максимальной и минамальной дробными частями = {}'.format( max_fract_n - min_fract_n ) )


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

a = int(input('Введите число '))
div = a
list_mod = []
while div > 0:
     quotient = div // 2
     mod = div % 2
     div = quotient
     list_mod.append(mod)

rev_list_mod = list_mod[::-1]
r = int(''.join(map(str, rev_list_mod)))
print('Число {} в двоичной системе счисления: {}'.format(a,r))
     



# #Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.def fibonacci(n): 
def fibonacci(n):
    current = 1
    if n > 2:
        current = fibonacci(n-1) + fibonacci(n-2)
    return current

element = input('k = ')
element = int(element)
numbers = []
numbersm = []
null = [0]
for i in range(1, element+1):
     value = fibonacci(i)
     valuev = fibonacci(i) * (-1) **(i+1)
     numbers.append(value)
     numbersm.append(valuev)
     numbersm_rev = list(reversed(numbersm))
print(numbersm_rev + null + numbers)

