# Создайте программу для игры в ""Крестики-нолики"".
l = [0,1,2,3,4,5,6,7,8]   
print('значения координат')
print(l[0],l[1],l[2])
print(l[3],l[4],l[5])
print(l[6],l[7],l[8])

gamer1 = input('Введите имя первого игрока: ')  
gamer2 = input('Введите имя второго игрока: ')
 
for i in range(9):
     if i % 2 ==0:
         x = gamer1
     else:
         x = gamer2
    
     print('{}, делайте ход'.format(x))
     k = int(input('введите координату  '))
     l[k] = (input('введите значение ячейки: в английской раскладке буквы x или o'))
      
     print(l[0],l[1],l[2])
     print(l[3],l[4],l[5])
     print(l[6],l[7],l[8])
    
     if (l[0]==l[1]==l[2] or l[3]==l[4]==l[5] or l[6]==l[7]==l[8] or l[0]==l[4]==l[8] or l[2]==l[4]==l[6] or l[0]==l[3]==l[6] or l[1]==l[4]==l[7] or l[2]==l[5]==l[8]):
        print('{}, вы выиграли'.format(x))
        break



    # Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
data = open (r'file3.txt', encoding='utf-8')
for i in data:
    print(i)
str=i
data.close()
def del_some_words(str):
    str = list(filter(lambda x: 'абв' not in x, str.split()))
    return " ".join(str)

str = del_some_words(str)
print(str)



# Создайте программу для игры с конфетами человек против человека.

import random

greeting = ('Правила игры: '
    'На столе лежит 2021 конфета, играют два игрока делая ход друг после друга. '
    'За один ход можно взять не более 28-ми. Все конфеты оппонента достаются сделавшему последний ход.')
            

messages = ['Ваша очередь брать конфеты', 'Возьмите конфеты', 'Ваш ход']


def play_game(n, m, players, messages):
    count = 0
    if n%10 == 1 and 9 > n > 10: letter = 'а'
    elif 1 < n%10 < 5 and 9 > n > 10: letter = 'ы'
    else: letter = ''
    while n > 0:
        print(f'{players[count%2]}, {random.choice(messages)}')
        move = int(input())
        if move > n or move > m:
            print(f'Можно взять не более {m} конфет{letter}, осталось всего {n} конфет{letter}')
            attempt = 3
            while attempt > 0:
                if n >= move <= m:
                    break
                print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                move = int(input())
                attempt -=1
            else: 
                return print(f'У Вас не осталось попыток.')
        n = n - move
        if n > 0: print(f'Осталось {n} конфет{letter}')
        else: print('Все конфеты разобраны.')
        count +=1
    return players[not count%2]

print(greeting)

player1 = input('Введите имя первого игрока\n')
player2 = input('Введите имя второго игрока\n')
players = [player1, player2]

n = int(2021)
m = int(28)

winer = play_game(n, m, players, messages)
if not winer:
    print('Победителя нет')
else: print(f'Победил {winer}! Ему достаются все конфеты!')
    


# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res

s = input("Введите текст для кодировки: ")
print(f"Текст после кодировки: {coding(s)}")
print(f"Текст после дешифровки: {decoding(coding(s))}")
