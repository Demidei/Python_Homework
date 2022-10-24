# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


def RLE_encode(path_file):
    f = open(path_file, "r+")
    s = f.read()
    Cou = 1
    head = 0
    temp = s[0]
    i = 1
    while i < (len(s)):
        if i < (len(s)) - 1:
            if s[i] == temp:
                Cou += 1
                i += 1
            else:
                s = s[:head] + str(Cou) + temp + s[i:]
                i = s.find(temp, head) + 1
                temp = s[i]
                head = i
                Cou = 1
                i = i + 1
        elif s[i] == temp:
            s = s[:head] + str(Cou + 1) + temp
            i = len(s)
        else:
            s = s[:head] + str(Cou) + temp + s[i:]
            s = s[:-1] + str(1) + s[-1]
            i = len(s)
    f.close()
    return s


def RLE_decode(path_file):
    f = open(path_file, "r+")
    s = f.read()
    temp = ""
    i = 0
    while i < (len(s)):
        if s[i].isdigit():
            temp = temp + s[i]
            i = i + 1
        else:
            Cou = int(temp)
            temp = ""
            for j in range(Cou):
                temp = temp + s[i]
            s = s.replace(str(Cou) + s[i], temp)
            i = s.find(temp) + Cou
            temp = ""
    f.close()
    return s


print("If you want to encode enter 'en' if you want to decode enter 'de'")
flag = input()
flag = flag.lower()
print()
if flag == "en":
    print(" input path")
    p = str(input())
    f = open("Encodedfile.txt", "w")
    f.write(RLE_encode(p))
    f.close()
elif flag == "de":
    print(" input path")
    p = str(input())
    f = open("Decodedfile.txt", "w")
    f.write(RLE_decode(p))
    f.close()
else:
    print("Error")
