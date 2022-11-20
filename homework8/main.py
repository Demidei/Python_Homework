import data_manager as da
import view as vi
import control as co

vi.greet()

da.jsonimport(da.departments,"datadep.json")

da.jsonimport(da.employees,"dataemp.json")

vector =-1

while vector !=0:
    vector=co.main_control()

da.jsonexport(da.departments,"datadep.json")
da.jsonexport(da.employees,"dataemp.json")

vi.end()

