# Задача 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# def string_edit(my_str, symbols):
#     return(' '.join([word for word in my_str.split() if symbols not in word]))


# input_str = input('Введите текст: ')
# text2 = input('Введите сочетание символов для удаления слов: ')
# print(string_edit(input_str, text2))

# input_str = input()
# text1 = 'абв'
# input_list = input_str.split()
# result_list = []
# for word in input_list:
#     if text1 not in word:
#         result_list.append(word)
# print(''.join(result_list))

# Задача 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# Человек против человека

from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = int(input("Введите количество конфет на столе: "))
flag = randint(0,2) # флаг очередности
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0 
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = input_dat(player2)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")

# Человек против бота -------------------------------------------------------------------------------

from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = "Bot"
value = int(input("Введите количество конфет на столе: "))
flag = randint(0,2) # флаг очередности
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0 
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = randint(1,29)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")

# человек против умного бота -------------------------------------------------

# вариант человек против бота c "интеллектом":
from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")


def bot_calc(value):
    k = randint(1,29)
    while value-k <= 28 and value > 29:
        k = randint(1,29)
    return k

player1 = input("Введите имя первого игрока: ")
player2 = "Bot"
value = int(input("Введите количество конфет на столе: "))
flag = randint(0,2) # флаг очередности
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0 
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = bot_calc(value)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")

# Задача 3. Создайте программу для игры в ""Крестики-нолики"".

# board = list(range(1,10))

# def design_board(board):
#     print('-'*12)
#     for i in range(3):
#         print('|', board[0+i*3],'|', board[1+i*3], '|', board[2+i*3], '|')
#         print('-'*12)

# # design_board(board)

# def choice(tic_tac):
#     valid = False
#     while not valid:
#         player_index = input('Выберите ячейку ' + tic_tac + ' --> ')
#         try:
#             player_index =int(player_index)
#         except:
#             print('Что-то не то нажали')
#             continue
#         if player_index >= 1 and player_index <= 9:
#             if(str(board[player_index-1]) not in 'XO'):
#                 board[player_index-1] = tic_tac
#                 valid = True
#             else:
#                 print('Занято')
#         else:
#             print('Еще раз попробуйте')

# def victory_check(board):
#     victory = ((0,1,2),(3,4,5),(6,7,8),
#                (0,3,6),(1,4,7),(2,5,8),
#                (0,4,8),(2,4,6))
#     for i in victory:
#         if board[i[0]] == board[i[1]] == board[i[2]]:
#             return board[i[0]]
#     return False

# def game(board):
#     counter =0
#     vic = False
#     while not vic:
#         design_board(board)
#         if counter % 2 == 0:
#             choice('X')
#         else:
#             choice('0')
#         counter +=1
#         if counter > 4:
#             tt_win = victory_check(board)
#             if tt_win:
#                 print(tt_win,'Победа')
#                 vic = True
#                 break
#             if counter == 9:
#                 print('Победила, ДРУЖБА)')
#         design_board(board)
# game(board)

# Задача 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.