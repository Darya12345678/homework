#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.def fibonacci(n): 
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

