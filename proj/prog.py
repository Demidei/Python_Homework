contacts = [
    { "fio": "ivan petrov", "phone": "12345" } ,
    { "fio": "max petrov", "phone": "12333345"},
    { "fio": "ivan petrov", "phone": "12333245"}  
]


def search(my_list,name):
     res=(filter( lambda s: s.get("fio").find(name)!=-1, my_list))
     
     list(map(print, res))

search(contacts,"petrov")
print()

def search2(my_list,name):
    list(map(print, filter( lambda s: s.get("fio").find(name)!=-1, my_list)))    

search2(contacts,"ivan")
print()

def show(my_list):
    list(map(print,  my_list))        

def add(my_list, name, number):
    temp_dict=dict( fio=name, phone=number)
    my_list.append(temp_dict)

add(contacts, "test", "111111")
print(contacts)
print()

def update(my_list, name, new_number, new_name ):
    for i in range(len(my_list)):
        if my_list[i].get("fio").find(name)!=-1:
            del my_list[i]
            add(my_list, new_name, new_number)
            
            
            


update(contacts, "ivan petrov", "123123","ivan petrov")
print(contacts)
print()
import csv
# def csvexport(my_list):
#     f = open("exports.csv","w")
    
#     file_writer  = csv.DictWriter(f, fieldnames=my_list[0].keys(),quoting=csv.QUOTE_NONNUMERIC)
#     file_writer.writeheader()
#     for i in range(len(my_list)):
#         file_writer.writerow(my_list[i])
#     f.close()

# csvexport(contacts)

# def csvimport(my_list):
#     f = open("exports.csv")
#     reader = csv.DictReader(f)
#     for row in reader:
#         my_list.append((row))
#     f.close()

# csvimport(contacts)
# show(contacts)
# print()

import json
# def jsonexport(my_list):
#     f = open("exports.json","w")
    
#     jsonstr=json.dumps(my_list,indent=4)
#     f.write(jsonstr)
#     f.close()

# jsonexport(contacts)

# def jsonimport(my_list):
#     f = open("exports.json")
#     jsonstr=((json.load(f)))
#     for i in range(len(jsonstr)):
#         my_list.append(jsonstr[i])

#     f.close()

# print("pars")
# jsonimport(contacts)
# show(contacts)
# print()

# def txtexport(my_list):
#     f = open("exports.txt","w")
#     for i in range(len(my_list)):
#         f.write(str(my_list[i])+ '\n')
#     f.close()

# txtexport(contacts)

# def txtimpoort(my_list):
#     f = open("exports.txt")
#     for line in f:
#         txtstr=line
#         txtdict={}
#         key = "fio"
#         value = txtstr[(txtstr.find("':")+4):(txtstr.find("',"))] 
#         txtdict[key] = value
#         key = "phone"
#         value = txtstr[((txtstr.find("':",txtstr.find("',")))+4):txtstr.find("'}")] 
#         txtdict[key] = value
#         my_list.append(dict(txtdict))
#     f.close

# print("pars")
# txtimpoort(contacts)
# show(contacts)
# print()

def delete_contact(my_list, name):
    for i in range(len(my_list)):
        if my_list[i].get("fio").find(name)!=-1:
            del my_list[i]

