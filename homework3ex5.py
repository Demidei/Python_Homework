# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.


def Fibb_and_neg(n):
    neg_fibb = [0]
    for i in range(n):
        if i < 2:
            neg_fibb.append(1)
        else:
            neg_fibb.append(neg_fibb[2 * i] + neg_fibb[2 * i - 1])
        neg_fibb.insert(0, neg_fibb[2 * i + 1] * ((-1) ** (i % 2)))
    return neg_fibb


print(" input number ", end="")
n = int(input())
print(Fibb_and_neg(n))
