# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

class Error(Exception):
    pass

class wrong_input(Error):
    pass

def Randomint_Fill(SubList):
    for i in range(N):
        random.seed
        SubList.append(random.randint((N*-1), N))

try:
    import random
    print(" input number ",end="")
    N = int(input())
    if (N < 1):
        raise wrong_input
    MyList=[]
    Randomint_Fill(MyList)
    f = open("file.txt", 'r')
    Sum=1
    for line in f:
        Sum *= MyList[int(line)]
    print(MyList)
    print("Multiplication of choosen elements is ", Sum)
except:
    print("Wrong or too small input")