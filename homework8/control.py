import crud as cr
import view as vi
import data_manager as da


def show_emp_in_dep_control():
    n=vi.seek_depart()
    if not n.isdigit:
        cr.search_depart_name(da.departments, da.employees,n)
    elif n!="0":
        cr.search_depart_id(da.departments, da.employees,n)

def depart_add_control():
    n=vi.adding_depart()
    if n!="0":
        cr.add_depart(da.departments, cr.search_max_id(da.departments)+1,n)
        vi.adding_depart_fin()

def empl_add_control():
    n1=vi.adding_emp_name()
    if n1!="0":
        n2=vi.adding_emp_salary()
        if n2!="0":
            cr.add_empl(da.employees,cr.search_max_id(da.employees)+1,n1,n2)
            vi.adding_empl_fin()

def transf_control():
    n1=vi.redacter1()
    if not n1.isdigit:
        n1=int(cr.empl_name_to_id(da.employees,n1))
    if n1!="0":
        n2=vi.redacter2()
        if not n2.isdigit:
            n2=int(cr.depart_name_to_id(da.departments,n2))
        if n2!="0": 
            cr.clear_empl(da.departments,n1)
            cr.appoint(da.departments, n1,n2)
            vi.redacterfin()

def delet_control():
    n=vi.deleter()
    if not n.isdigit:
        n=int(cr.empl_name_to_id(da.employees,n))
    if n!="0":
        cr.clear_empl(da.departments,n)
        cr.del_empl(da.employees,n) 
        vi.deleterfin()
    

def show_dep_control():
    cr.show(da.departments)

def show_empl_control():
    cr.show(da.employees)




main_menu={
    1: show_dep_control,
    2: show_empl_control,
    3: show_emp_in_dep_control,
    4: depart_add_control,
    5: empl_add_control, 
    6: transf_control,
    7: delet_control,


}



def main_control():
    n=int(vi.action())
    main_menu.get(n)()
    n=int(vi.operationend())
    return n

