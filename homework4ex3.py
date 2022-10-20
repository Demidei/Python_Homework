# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random


def random_int_fill(sublist, n):
    for i in range(n):
        random.seed
        sublist.append(random.randint((n * -1), n))


def uniq_numbers(sublist):
    uniq_list = []
    for i in range(len(sublist)):
        if sublist.count(sublist[i]) == 1:
            uniq_list.append(sublist[i])
    return uniq_list


print(" input size of list ", end="")
n = int(input())
my_list = []
random_int_fill(my_list, n)
print(my_list)
print(uniq_numbers(my_list))

# Можно сделать без count


def alt_uniq_numbers(sublist):
    uniq_list = []
    temp_list = []
    temp_list.extend(sublist)
    for i in range(len(sublist)):
        flag = 0
        temp_len = len(temp_list)
        j = 0
        while j < temp_len:
            if temp_list[j] == sublist[i]:
                del temp_list[j]
                flag += 1

                temp_len -= 1
            j += 1
        if flag == 1:
            uniq_list.append(sublist[i])

    return uniq_list
