# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

class Error(Exception):
    pass

class wrong_input(Error):
    pass

try:
    print(" input number ",end="")
    N = int(input())
    if (N < 1):
        raise wrong_input
    MyList=[1]
    for i in range(N - 1):
        MyList.append(MyList[i] * ( i + 2))
    print(MyList)
except:
    print("Input error")