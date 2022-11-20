
import json

global employees
employees=[    ]
global departments
departments=[]

def jsonexport(my_list,path):
    f = open(path, "w")

    jsonstr = json.dumps(my_list, indent=4)
    f.write(jsonstr)
    f.close()


def jsonimport(my_list,path):
    f = open(path)
    jsonstr = json.load(f)
    for i in range(len(jsonstr)):
        my_list.append(jsonstr[i])

    f.close()

