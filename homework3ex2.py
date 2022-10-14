# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random


def random_int_fill(sub_list, size):
    for i in range(size):
        random.seed
        sub_list.append(random.randint((size * -1), size))


def pair_multi(sub_list):
    result_list = []
    i = 0
    while i <= len(sub_list) - i - 1:
        result_list.append(sub_list[i] * sub_list[len(sub_list) - i - 1])
        i += 1
    return result_list


print(" input size of list ", end="")
n = int(input())
my_list = []
random_int_fill(my_list, n)
print(my_list)
print(pair_multi(my_list))
