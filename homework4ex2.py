# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def prime_numbers(n):
    prime_list = []
    while n > 1:
        temp = 2
        while n % temp != 0:
            temp += 1
        prime_list.append(temp)
        n = n / temp
    return prime_list


print(" input number ", end="")
n = int(input())
print(prime_numbers(n))
