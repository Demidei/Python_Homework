# Создайте программу для игры с конфетами человек против человека. Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

import random


def candy_game():
    player = random.randint(1, 2)
    candy = 2021
    print("There are ", str(candy), " candies on the table")
    while candy > 0:
        if player == 1:
            player = 2
        else:
            player = 1
        turn = 0
        while turn < 1 or turn > 28 or turn > candy:
            print("Player ", str(player), " is your turn")
            print("How many candies Player ", str(player), " will take? ")
            turn = int(input())
            if turn < 1 or turn > 28 or turn > candy:
                print(
                    "In one turn, you can take no more than 28 candies and no less than one! And only ",
                    str(candy),
                    " candies left",
                )
        candy = candy - turn
        print()
        print(str(candy), " candies left")
        print()
    print("Player ", str(player), " wins!")


def candy_game_bot():
    player = random.randint(1, 2)
    candy = 2021
    print("There are ", str(candy), " candies on the table")
    turn = 0
    while candy > 0:
        if player == 1:
            player = 2
        else:
            player = 1
            turn = 0
        if player == 1:
            while turn < 1 or turn > 28 or turn > candy:
                print("Player 1 is your turn")
                print("How many candies Player 1 will take? ")
                turn = int(input())
                if turn < 1 or turn > 28 or turn > candy:
                    print(
                        "In one turn, you can take no more than 28 candies and no less than one! And only ",
                        str(candy),
                        " candies left",
                    )
        else:
            print("Now it's the bot's turn")
            if candy < 29:
                turn = candy
            elif candy % 29 != 0:
                turn = candy % 29
            else:
                random.seed
                turn = random.randint(1, 28)
            print("The bot took ", str(turn), " candies")
        candy = candy - turn
        print()
        print(str(candy), " candies left")
        print()
    if player == 1:
        print("Player 1 wins!")
    else:
        print("Bot wins!")


print(
    "If you want to play with a bot enter 'bot' if you want to play together enter 'hot seat'"
)
flag = input()
flag = flag.lower()
print()
if flag == "bot":
    candy_game_bot()
elif flag == "hot seat":
    candy_game()
else:
    print("Error")
