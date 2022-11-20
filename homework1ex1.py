# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

print(" input number of day ",end="")
N=int(input())
if(N<1 or N>7):
    print("Error")
elif(N<6):
    print("No, is not day off")
else:
    print("Yes, is day off")