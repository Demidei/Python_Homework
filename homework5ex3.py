# Создайте программу для игры в ""Крестики-нолики"".


import random


def turn(tu, N, game_field):
    match N:
        case 1:
            if game_field[2][0] == "| ":
                game_field[2][0] = tu
                flag = True
            else:
                print("Error")
                flag = False
        case 2:
            if game_field[2][1] == "| ":
                game_field[2][1] = tu
                flag = True
            else:
                print("Error")
                flag = False
        case 3:
            if game_field[2][2] == "| ":
                game_field[2][2] = tu
                flag = True
            else:
                print("Error")
                flag = False
        case 4:
            if game_field[1][0] == "| ":
                game_field[1][0] = tu
                flag = True
            else:
                print("Error")
                flag = False
        case 5:
            if game_field[1][1] == "| ":
                game_field[1][1] = tu
                flag = True
            else:
                print("Error")
                flag = False
        case 6:
            if game_field[1][2] == "| ":
                game_field[1][2] = tu
                flag = True
            else:
                print("Error")
                flag = False
        case 7:
            if game_field[0][0] == "| ":
                game_field[0][0] = tu
                flag = True
            else:
                print("Error")
                flag = False
        case 8:
            if game_field[0][1] == "| ":
                game_field[0][1] = tu
                flag = True
            else:
                print("Error")
                flag = False
        case 9:
            if game_field[0][2] == "| ":
                game_field[0][2] = tu
                flag = True
            else:
                print("Error")
                flag = False
        case _:
            print("Error")
            print("Error")
            flag = False
    return flag


def end_game_condition(game_field, tu):
    flag = False
    for i in range(len(game_field)):
        for j in range(len(game_field[i])):
            if game_field[i][j] == "| ":
                flag = True
    if flag == False:
        print("Game over. It is Tie")
        game_over = True
    elif (
        (
            game_field[0][0] == tu
            and (game_field[0][0] == game_field[0][1] == game_field[0][2])
        )
        or (
            game_field[1][0] == tu
            and (game_field[1][0] == game_field[1][1] == game_field[1][2])
        )
        or (
            game_field[2][0] == tu
            and (game_field[2][0] == game_field[2][1] == game_field[2][2])
        )
        or (
            game_field[0][0] == tu
            and (game_field[0][0] == game_field[1][0] == game_field[2][0])
        )
        or (
            game_field[0][1] == tu
            and (game_field[0][1] == game_field[1][1] == game_field[2][1])
        )
        or (
            game_field[0][2] == tu
            and (game_field[0][2] == game_field[1][2] == game_field[2][2])
        )
        or (
            game_field[0][0] == tu
            and (game_field[0][0] == game_field[1][1] == game_field[2][2])
        )
        or (
            game_field[2][0] == tu
            and (game_field[2][0] == game_field[1][1] == game_field[0][2])
        )
    ):
        print("Game over.", tu[-1], " win")
        game_over = True
    else:
        game_over = False
    return game_over


def tic_tac_toe():
    tu = "|O"
    m = 3
    n = 3
    print(
        "Use digit to make your turn: 1 - Left Down, 2 - Centre Down, 3 - Right Down, 4 - Left Mid, 5 - Centre Mid, 6 - Right Mid, 7 - Left Up, 8 - Centre Up, 9 - Right Up"
    )
    game_field = [["|7", "|8", "|9"], ["|4", "|5", "|6"], ["|1", "|2", "|3"]]
    for i in range(len(game_field)):
        for j in range(len(game_field[i])):
            print(game_field[i][j], end="|")
        print()
    print()
    game_field = [["| "] * m for i in range(n)]
    for i in range(len(game_field)):
        for j in range(len(game_field[i])):
            print(game_field[i][j], end="|")
        print()
    print()
    while end_game_condition(game_field, tu) != True:
        if tu == "|X":
            tu = "|O"
        else:
            tu = "|X"
        print(tu[-1], "turn now")
        print(
            "Use digit to make your turn: 1 - Left Down, 2 - Centre Down, 3 - Right Down, 4 - Left Mid, 5 - Centre Mid, 6 - Right Mid, 7 - Left Up, 8 - Centre Up, 9 - Right Up"
        )
        N = int(input())
        while turn(tu, N, game_field) != True:
            print(
                "Use digit to make your turn: 1 - Left Down, 2 - Centre Down, 3 - Right Down, 4 - Left Mid, 5 - Centre Mid, 6 - Right Mid, 7 - Left Up, 8 - Centre Up, 9 - Right Up"
            )
            N = int(input())
        for i in range(len(game_field)):
            for j in range(len(game_field[i])):
                print(game_field[i][j], end="|")
            print()
        print()


def try_to_win(game_field, me):
    flag = False
    lines = [
        [[0, 0], [0, 1], [0, 2]],
        [[1, 0], [1, 1], [1, 2]],
        [[2, 0], [2, 1], [2, 2]],
        [[0, 0], [1, 0], [2, 0]],
        [[0, 1], [1, 1], [2, 1]],
        [[0, 2], [1, 2], [2, 2]],
        [[0, 0], [1, 1], [2, 2]],
        [[2, 0], [1, 1], [0, 2]],
    ]
    for i in range(len(lines)):
        cou = 0
        mark = -1
        for j in range(len(lines[i])):
            if game_field[lines[i][j][0]][lines[i][j][1]] == "| ":
                mark = [i, j]
            elif game_field[lines[i][j][0]][lines[i][j][1]] == me:
                cou += 1
            if cou == 2 and mark != -1:
                game_field[lines[mark[0]][mark[1]][0]][lines[mark[0]][mark[1]][1]] = me
                flag = True
                break
    return flag


def try_not_to_lose(game_field, me, not_me):
    flag = False
    lines = [
        [[0, 0], [0, 1], [0, 2]],
        [[1, 0], [1, 1], [1, 2]],
        [[2, 0], [2, 1], [2, 2]],
        [[0, 0], [1, 0], [2, 0]],
        [[0, 1], [1, 1], [2, 1]],
        [[0, 2], [1, 2], [2, 2]],
        [[0, 0], [1, 1], [2, 2]],
        [[2, 0], [1, 1], [0, 2]],
    ]
    for i in range(len(lines)):
        cou = 0
        mark = -1
        for j in range(len(lines[i])):
            if game_field[lines[i][j][0]][lines[i][j][1]] == "| ":
                mark = [i, j]
            elif game_field[lines[i][j][0]][lines[i][j][1]] == not_me:
                cou += 1
            if cou == 2 and mark != -1:
                game_field[lines[mark[0]][mark[1]][0]][lines[mark[0]][mark[1]][1]] = me
                flag = True
                break
    return flag


def just_try(game_field, me):
    angle = [[0, 0], [0, 2], [2, 0], [2, 2]]
    cross = [
        [[1, 0], [0, 1], [0, 2], [2, 2]],
        [[0, 1], [1, 2], [0, 0], [2, 2]],
        [[1, 0], [2, 1], [0, 0], [0, 2]],
        [[2, 1], [1, 2], [0, 2], [0, 0]],
    ]

    if (game_field[1][1]) == "| ":
        game_field[1][1] = me
        flag = True
    else:
        flag = False
        for i in range(len(angle)):
            if (game_field[angle[i][0]][angle[i][1]]) == "| " and (
                game_field[cross[i][0][0]][cross[i][0][1]] == "| "
                and game_field[cross[i][1][0]][cross[i][1][1]] == "| "
                and game_field[cross[i][2][0]][cross[i][2][1]] == "| "
                and game_field[cross[i][3][0]][cross[i][3][1]] == "| "
            ):
                game_field[angle[i][0]][angle[i][1]] = me
                flag = True
                break
        if flag == False:
            for i in range(len(angle)):
                if (game_field[angle[i][0]][angle[i][1]]) == "| ":
                    game_field[angle[i][0]][angle[i][1]] = me
                    flag = True
                    break
        if flag == False:
            for i in range(len(game_field)):
                 for j in range(len(game_field[i])):
                        if (game_field[i][j]) == "| ":
                              game_field[i][j]=me
                              flag = True
                              break
                 if flag == True:
                    break
    return flag




def tic_tac_toe_bot():
    player = random.randint(1, 2)
    if player == 1:
        me = "|O"
        not_me = "|X"
        tu = me
    else:
        me = "|X"
        not_me = "|O"
        tu = not_me

    m = 3
    n = 3
    print(
        "Use digit to make your turn: 1 - Left Down, 2 - Centre Down, 3 - Right Down, 4 - Left Mid, 5 - Centre Mid, 6 - Right Mid, 7 - Left Up, 8 - Centre Up, 9 - Right Up"
    )
    game_field = [["|7", "|8", "|9"], ["|4", "|5", "|6"], ["|1", "|2", "|3"]]
    for i in range(len(game_field)):
        for j in range(len(game_field[i])):
            print(game_field[i][j], end="|")
        print()
    print()
    game_field = [["| "] * m for i in range(n)]
    for i in range(len(game_field)):
        for j in range(len(game_field[i])):
            print(game_field[i][j], end="|")
        print()
    print()
    while end_game_condition(game_field, tu) != True:
        if tu == "|X":
            tu = "|O"
        else:
            tu = "|X"
        if tu == me:
            print(tu[-1], "turn now")
            if try_to_win(game_field, me) == False:
                if try_not_to_lose(game_field, me, not_me) == False:
                   if just_try(game_field, me)==False:
                    print("wrong", end="|")
            for i in range(len(game_field)):
                for j in range(len(game_field[i])):
                    print(game_field[i][j], end="|")
                print()
            print()
        else:
            print(tu[-1], "turn now")
            print(
                "Use digit to make your turn: 1 - Left Down, 2 - Centre Down, 3 - Right Down, 4 - Left Mid, 5 - Centre Mid, 6 - Right Mid, 7 - Left Up, 8 - Centre Up, 9 - Right Up"
            )
            N = int(input())
            while turn(tu, N, game_field) != True:
                print(
                    "Use digit to make your turn: 1 - Left Down, 2 - Centre Down, 3 - Right Down, 4 - Left Mid, 5 - Centre Mid, 6 - Right Mid, 7 - Left Up, 8 - Centre Up, 9 - Right Up"
                )
                N = int(input())
            for i in range(len(game_field)):
                for j in range(len(game_field[i])):
                    print(game_field[i][j], end="|")
                print()
            print()


print(
    "If you want to play with a bot enter 'bot' if you want to play together enter 'hot seat'"
)
flag = input()
flag = flag.lower()
print()
if flag == "bot":
    tic_tac_toe_bot()
elif flag == "hot seat":
    tic_tac_toe()
else:
    print("Error")
