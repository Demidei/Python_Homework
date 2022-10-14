# Напишите программу, которая будет преобразовывать десятичное число в двоичное.


def bin_conv_int(n, st=""):
    if n > 1:
        st = st + bin_conv_int(n // 2, st) + str(n % 2)
        return st
    else:
        return "1"


print(" input number ", end="")
n = int(input())
print("Binary representation of", n, " is ", bin_conv_int(n))
