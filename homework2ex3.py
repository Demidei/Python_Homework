# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

print(" input number ",end="")
N = int(input())
MyList=[]
Sum=0
for i in range(N):
    MyList.append((1+(1/(i+1)))**(i+1))
    Sum += MyList[i]
print(MyList)
print("Sum of sequence is ", Sum)