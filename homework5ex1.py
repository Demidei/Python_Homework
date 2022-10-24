# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


def seeker(seek, path_file):
    f = open(path_file, "r+")
    s = f.read()
    s = s.split()
    res_list = []
    for i in s:
        if seek not in i:
            res_list.append(i)
    f.close
    return str(" ".join(res_list))


print(" input substring to delete ", end="")
seek = str(input())
f = open("Seekedfree.txt", "w")
f.write(seeker(seek, "fileabc.txt"))
f.close()
