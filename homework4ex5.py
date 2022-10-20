# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


def polynom_analysis(listcoef, listdegree, path_file):
    f = open(path_file, "r+")
    s = f.read()

    while s.find("x") != -1:
        temp = ""
        i = s.find("x") - 1
        while i > -1:
            temp = s[i] + temp
            s = s[:i] + s[i + 1 :]
            i = i - 1
        listcoef.append(int(temp))
        i = s.find("x") + 2
        if s[i - 1] != "^":
            temp = "1"
        else:
            temp = ""
            while s[i] != "+" and s[i] != "-":
                temp = temp + s[i]
                s = s[:i] + s[i + 1 :]
        listdegree.append(int(temp))
        i = s.find("x")
        s = s[:i] + s[i + 1 :]
        if s.find("^") != -1:
            i = s.find("^")
            s = s[:i] + s[i + 1 :]
    if listdegree[-1] != 0:
        temp = ""
        i = s.find("=") - 1
        if i < 0:
            listcoef.append(0)
        else:
            while i > -1:
                temp = s[i] + temp
                s = s[:i] + s[i + 1 :]
                i = i - 1
            listcoef.append(int(temp))
        listdegree.append(0)
    f.close


def polynom_sum(coef1, degree1, coef2, degree2):
    poly_sum_str = ""
    while degree1[0] != 0 or degree2[0] != 0:
        if (degree1[0]) == (degree2[0]):
            if coef1[0] + coef2[0] != 0:
                poly_sum_str = poly_sum_str + str(coef1[0] + coef2[0]) + "x"
                if degree1[0] != 1:
                    poly_sum_str = poly_sum_str + "^" + str(degree1[0]) + "+"
                else:
                    poly_sum_str = poly_sum_str + "+"
            del degree1[0]
            del degree2[0]
            del coef1[0]
            del coef2[0]
        elif degree1[0] > degree2[0]:
            if coef1[0] != 0:
                poly_sum_str = poly_sum_str + str(coef1[0]) + "x"
                if degree1[0] != 1:
                    poly_sum_str = poly_sum_str + "^" + str(degree1[0]) + "+"
                else:
                    poly_sum_str = poly_sum_str + "+"
            del degree1[0]
            del coef1[0]
        else:
            if coef2[0] != 0:
                poly_sum_str = poly_sum_str + str(coef2[0]) + "x"
                if degree2[0] != 1:
                    poly_sum_str = poly_sum_str + "^" + str(degree2[0]) + "+"
                else:
                    poly_sum_str = poly_sum_str + "+"
            del degree2[0]
            del coef2[0]
    if coef1[0] + coef2[0] != 0:
        poly_sum_str = poly_sum_str + str(coef1[0] + coef2[0]) + "=0"
    else:
        poly_sum_str = poly_sum_str + "=0"
    poly_sum_str = poly_sum_str.replace("+-", "-")
    return poly_sum_str


listcoef1 = []
listdegree1 = []
listcoef2 = []
listdegree2 = []
polynom_analysis(listcoef1, listdegree1, "file1.txt")
polynom_analysis(listcoef2, listdegree2, "file2.txt")
f = open("Polynomesum.txt", "w")
f.write(polynom_sum(listcoef1, listdegree1, listcoef2, listdegree2))
f.close()
