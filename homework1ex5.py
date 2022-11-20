# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

print(" input X1 of first point ",end="")
X1=int(input())
print(" input Y1 of first point ",end="")
Y1=int(input())
print(" input X2 of second point ",end="")
X2=int(input())
print(" input Y2 of second point ",end="")
Y2=int(input())
print("Distance between points is ", round((((X1-X2)*(X1-X2))+((Y1-Y2)*(Y1-Y2)))**(1/2),3))