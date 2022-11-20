# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

print(" input X ",end="")
X=int(input())
if(X==0):
    print("Error")
    exit()
print(" input Y ",end="")
Y=int(input())
if(Y==0):
    print("Error")
    exit()
if(X>0):
    if(Y>0):
        print("First quarter")
    else:
        print("Fourht quarter")
elif(Y>0):
    print("Second quarter")
else:
    print("Third quarter")
