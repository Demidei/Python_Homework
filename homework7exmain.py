import homework7exmethods as mi
import homework7exview as vi
import homework7exdata as da

vi.greet()
vector=99

while vector!=0:
    vector=int(vi.action())
    match vector:
        case 1:
            mi.show(da.contacts)
            print()

        case 2:
            name=vi.seek()
            if name=="0":
                print()

            else:
                mi.search(da.contacts,name)
                print()
                
            del name
        case 3:
            name=vi.adding()
            if name=="0":
                print()
                
            else:
                mi.add(da.contacts,name[0],name[1])
                print()
                vi.addingfin()
                
            del name
        case 4:
            name=vi.redacter1()
            if name=="0":
                print()
               
            else:
                temp=vi.redacter2()
                if temp=="0":
                    print()
                   
                else:
                    if temp[0]=="-1" and temp[1]=="-1":
                        print()
                        vi.addingfin()
                   
                    else: 
                        if temp[0]=="-1":
                            mi.update1(da.contacts,name,temp[1])
                            print()
                            vi.addingfin()
              
                        else:
                           if temp[1]=="-1":
                                mi.update2(da.contacts,name,temp[0])
                                print()
                                vi.addingfin()
                   
                           else:
                                mi.update0(da.contacts,name,temp[1], temp[0])
                                print()
                                vi.addingfin()
          
                del temp                   
            del name
                            
        case 5:
            name=vi.deleter()
            if name=="0":
                print()
   
            else:
                mi.delete_contact(da.contacts,name)
                print()
                vi.deleterfin()
   
            del name
        case 6:
            temp=vi.exporter1()
            if temp=="0":
                print()
    
            else:
                match temp:
          
                          case "1":
                                name=vi.exporter2()
                                if name=="0":
                                       print()
                 
                                else:                                 
                                    mi.txtexport(da.contacts,name)
                                    print()
                                    vi.exporterfin()
           
                                del name    
                          case "2":
                                name=vi.exporter2()
                                if name=="0":
                                       print()
          
                                else:                                 
                                    mi.csvexport(da.contacts,name)
                                    print()
                                    vi.exporterfin()
                                         
                                del name        
                          case "3":
                                name=vi.exporter2()
                                if name=="0":
                                       print()
                          
                                else:                                 
                                    mi.jsonexport(da.contacts,name)
                                    print()
                                    vi.exporterfin()
                
                                del name    
                          case _:                                          
                                print("Ошибка!")
                                print()
            
            del temp                    
        case 7:
            temp=vi.importer1()
            if temp=="0":
                print()
        
            else:
                match temp:

            
                          case "1":
                                name=vi.importer2()
                                if name=="0":
                                       print()
                  
                                else:                                 
                                    mi.txtimport(da.contacts,name)
                                    print()
                                    vi.importerfin()
                
                                del name
                          case "2":
                                name=vi.importer2()
                                if name=="0":
                                       print()
    
                                else:                                 
                                    mi.csvimport(da.contacts,name)
                                    print()
                                    vi.importerfin()
      
                                del name                               
                          case "3":
                                name=vi.importer2()
                                if name=="0":
                                       print()
                   
                                else:                                 
                                    mi.jsonimport(da.contacts,name)
                                    print()
                                    vi.importerfin()
                 
                                del name 
                          case _:                                          
                                print("Ошибка!")
                                print()
          
            del temp                                                             
        case _:
            print("Ошибка!")
            print()
    vector=int(vi.operationend())
    print()
vi.end()