string = input('Введите вещественное число: ').split('.')
a = string[1]
b = string[0]
a = int(a)
b = int(b)
n = a
d = 1
m = b
y = 1
sumleftpart = 0
sumrightpart = 0
while n > 0:
    d  = n % 10
    n = n // 10
    sumleftpart += d
    # print(d, n)
while m > 0:
    y = m % 10
    m = m // 10
    sumrightpart += y
    # print(y, m)

print(sumleftpart + sumrightpart)
 





 