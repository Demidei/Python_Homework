# Создайте программу для игры в ""Крестики-нолики"".




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
    flag=False
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




tic_tac_toe()
