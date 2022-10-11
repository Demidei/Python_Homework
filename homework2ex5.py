# Реализуйте алгоритм перемешивания списка.

import random

def Randomint_Fill(SubList):
    for i in range(N):
        random.seed
        SubList.append(random.randint((N*-1), N))

def MyShaffle(SubList):
    for i in range(N):
        random.seed
        temp=random.randint(0, (N-i-1))
        SubList.append(SubList[temp])
        del SubList[temp]


print(" input number ",end="")
N = int(input())
MyList=[]
Randomint_Fill(MyList)
print(MyList)
MyShaffle(MyList)
print(MyList)