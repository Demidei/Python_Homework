# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random


def polynome_string(n):
    poly_str = "=0"
    for i in range(n):
        temp_coef = random.randint(0, 100)
        if temp_coef != 0:
            if i > 0:
                poly_str = str(temp_coef) + "x^" + str(i) + "+" + poly_str
            elif i == 0:
                poly_str = str(temp_coef) + poly_str
            else:
                poly_str = str(temp_coef) + "x" + "+" + poly_str

    return poly_str


print(" input degree ", end="")
n = int(input())
# print(polynome_string(n))
f = open("Polynome.txt", "w")
f.write(polynome_string(n))
f.close()
