import csv


import json


def search(my_list, name):
    list(map(print, filter(lambda s: s.get("fio").find(name) != -1, my_list)))


def show(my_list):
    list(map(print, my_list))


def add(my_list, name, number):
    temp_dict = dict(fio=name, phone=number)
    my_list.append(temp_dict)


def update0(my_list, name, new_number, new_name):
    for i in range(len(my_list)):
        if my_list[i].get("fio").find(name) != -1:
            del my_list[i]
            add(my_list, new_name, new_number)

def update1(my_list, name, new_number):
    for i in range(len(my_list)):
        if my_list[i].get("fio").find(name) != -1:
            del my_list[i]
            add(my_list, name, new_number)

def update2(my_list, name,  new_name):
    for i in range(len(my_list)):
        if my_list[i].get("fio").find(name) != -1:
            new_number= my_list[i].get("phone")
            del my_list[i]
            add(my_list, new_name, new_number)


def csvexport(my_list, path):
    f = open(path, "w")

    file_writer = csv.DictWriter(
        f, fieldnames=my_list[0].keys(), quoting=csv.QUOTE_NONNUMERIC
    )
    file_writer.writeheader()
    for i in range(len(my_list)):
        file_writer.writerow(my_list[i])
    f.close()


def csvimport(my_list, path):
    f = open(path)
    reader = csv.DictReader(f)
    for row in reader:
        my_list.append((row))
    f.close()


def jsonexport(my_list, path):
    f = open(path, "w")

    jsonstr = json.dumps(my_list, indent=4)
    f.write(jsonstr)
    f.close()


def jsonimport(my_list, path):
    f = open(path)
    jsonstr = json.load(f)
    for i in range(len(jsonstr)):
        my_list.append(jsonstr[i])

    f.close()


def txtexport(my_list, path):
    f = open(path, "w")
    for i in range(len(my_list)):
        f.write(str(my_list[i]) + "\n")
    f.close()


def txtimport(my_list, path):
    f = open(path)
    for line in f:
        txtstr = line
        txtdict = {}
        key = "fio"
        value = txtstr[(txtstr.find("':") + 4) : (txtstr.find("',"))]
        txtdict[key] = value
        key = "phone"
        value = txtstr[((txtstr.find("':", txtstr.find("',"))) + 4) : txtstr.find("'}")]
        txtdict[key] = value
        my_list.append(dict(txtdict))
    f.close


def delete_contact(my_list, name):
    for i in range(len(my_list)):
        if my_list[i].get("fio").find(name) != -1:
            del my_list[i]

