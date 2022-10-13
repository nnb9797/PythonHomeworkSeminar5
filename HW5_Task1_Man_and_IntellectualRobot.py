#1. Создайте программу для игры с конфетами человек против человека.Условие задачи:
# На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

# Умный Робот против человека:

from random import randint

def input_sweets(name):
    x = int(input(f"Игрок {name}, введите количество конфет, которое хотите взять, от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"Игрок {name}, введите корректное количество конфет от 1 до 28: "))
    return x

def game_print(name, taken, counter, sw_number):
    print(f"Ходил {name}, он взял {taken}, теперь у него {counter}. Теперь на столе {sw_number} конфет.")

def Robot_plays(sw_number):
    taken = randint(1,28)
    while sw_number-taken <= 28 and sw_number > 28:
        taken = randint(1,28)
    return taken

player1 = input("Введите имя первого игрока: ")
player2 = "Robot"
sw_number = 2021
turn = randint(0,2)
if turn:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0
counter2 = 0

while sw_number > 28:
    if turn:
        taken = input_sweets(player1)
        counter1 += taken
        sw_number -= taken
        turn = False
        game_print(player1, taken, counter1, sw_number)
    else:
        taken = Robot_plays(sw_number)
        counter2 += taken
        sw_number -= taken
        turn = True
        game_print(player2, taken, counter2, sw_number)

if turn:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")