# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import random


def random_int_fill(sub_list, size):
    for i in range(size):
        random.seed
        sub_list.append(random.randint((size * -1), size))


def odd_index_sum(sub_list):
    odd_sum = 0
    i = 1
    while i < len(sub_list):
        odd_sum += sub_list[i]
        i += 2
    return odd_sum


print(" input size of list ", end="")
n = int(input())
my_list = []
random_int_fill(my_list, n)
print(my_list)
print("Sum of odd elements is", odd_index_sum(my_list))
