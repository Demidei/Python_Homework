# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

import random


def random_float_fill(sub_list, size):
    for i in range(size):
        random.seed
        sub_list.append(random.uniform((size * -1), size))


def farctional_part_amplitude(sub_list):
    min_part = abs(sub_list[0]) % 1
    max_part = min_part
    for i in range(len(sub_list) - 1):
        if sub_list[i + 1] % 1 != 0:
            if min_part > abs(sub_list[i + 1]) % 1:
                min_part = abs(sub_list[i + 1]) % 1
            if max_part < abs(sub_list[i + 1]) % 1:
                max_part = abs(sub_list[i + 1] % 1)
    return max_part - min_part


print(" input size of list ", end="")
N = int(input())
my_list = []
random_float_fill(my_list, N)
print(my_list)
print(
    "Difference between fractional parts of a number is ",
    farctional_part_amplitude(my_list),
)
