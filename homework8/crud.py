
def search_name(my_list, crit):
    list(map(print, filter(lambda s: s.get("fio").find(crit) != -1, my_list)))

def search_id(my_list, crit):
    list(map(print, filter(lambda s: s.get("id")== crit, my_list)))    


def search_depart_id(my_list1,my_list2, crit):
    search_zone=list(filter(lambda s: s.get("id")== crit, my_list1))
    for i in range(len(search_zone)):
        print(search_zone[i].get("name"))
        for j in  range(len(search_zone[i].get("employees"))):
            list(map(print, filter(lambda s: s.get("id")== search_zone[i].get("employees")[j], my_list2)))  

def search_depart_name(my_list1,my_list2, crit):
    search_zone=list(filter(lambda s: s.get("name").find(crit) != -1, my_list1))
    for i in range(len(search_zone)):
        print(search_zone[i].get("name"))
        for j in  range(len(search_zone[i].get("employees"))):
            list(map(print, filter(lambda s: s.get("id")== search_zone[i].get("employees")[j], my_list2)))  

def show(my_list):
    list(map(print, my_list))


def add_depart(my_list, id,  name):
    temp_dict = dict(id=id, name=name)
    my_list.append(temp_dict)

def add_empl(my_list, id,  fio, salary):
    temp_dict = dict(id=id, fio=fio, salary=salary)
    my_list.append(temp_dict)    

def search_max_id(my_list):
    n=0 
    for i in  range(len(my_list)):
        if n<my_list[i].get("id"):
            n=my_list[i].get("id")
    return   n  

def empl_name_to_id(my_list, crit):
    for i in  range(len(my_list)):
        if my_list[i].get("fio").find(crit) != -1:
            n=my_list[i].get("id")
            break
    return   n  

def depart_name_to_id(my_list, crit):
    for i in  range(len(my_list)):
        if my_list[i].get("name").find(crit) != -1:
            n=my_list[i].get("id")
            break
    return   n  

def clear_empl(my_list,id_empl):
    for i in  range(len(my_list)):
        for j in range(len(list(my_list[i].get("employees")))):
            if my_list[i].get("employees")[j]==id_empl:
                my_list[i].get("employees").pop(j)


def appoint(my_list,id_empl,id_depart):
    for i in range(len(my_list)):
        if my_list[i].get("id")==id_depart:
            my_list[i].get("employees").append(int(id_empl))


def del_empl(my_list, crit):
    for i in range(len(my_list)):
        if my_list[i].get("id")== crit:
            del my_list[i]

