# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
            # Исходная задача.
# num = [1, 2, 7, 5, 6]
# rev_num = num[::-1]

# if len(num) % 2 == 0:
#      num_pairs = (len(num)) // 2
# else:
#      num_pairs = ((len(num)) + 1) // 2

# result = []
# for j in range (num_pairs) :
#       res = num[j] * rev_num[j]
#       result.append(res)

# print('Произведение пар чисел:', result)

   
           # Задача с Lambda.
num = [1, 2, 7, 5, 6]
rev_num = num[::-1]

if len(num) % 2 == 0:
     num_pairs = (len(num)) // 2
else:
     num_pairs = ((len(num)) + 1) // 2

res = lambda x : num[x] * rev_num[x]

result = [ res(j) for j in range(num_pairs) ]

print('Произведение пар чисел:', result)

          
# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.
  
         # Исходная задача.
# list = [2, 3, 7, 6, 8]
# a = list[1::2]
# print ('На нечетных индексах элементы ',a)
# sum = 0
# for i in (a):
#     sum += i

# print('Сумма элементов на нечетных индексах =', sum )


         #Задача с Filter

list = [2, 3, 7, 6, 8]
a = list(filter(lambda x: not x % 2, list))
for i in (a):
    sum += i

print('Сумма элементов на нечетных индексах =', sum )

   

# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]

         # Исходная задача
a = [1,1,2,3,4,4,4]
r = []
for i in a:
   if a.count(i) == 1:
     r.append(i) 

print(r)


         # Задача с List Comprehension
a = [1,1,2,3,4,4,4]
r = [i for i in a if a.count(i)==1]

print(r)





