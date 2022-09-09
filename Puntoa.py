from mimetypes import init
from pickle import TRUE


class Supermarket:
    def __init__(self,name):
        self.name= name
        self.dictDairy={}
        self.dictGrain={}
        self.dictCleaning={}
         
            
    def imprimr(self):
        print(self.dictDairy)
        print(self.dictGrain)
        print(self.dictCleaning)
              
    def askDairy(self):
        listDairy=[]
        listCantDairy=[]
        bandera= TRUE
        while bandera:
            try:
                allDairy=int(input('cuantas clases de lacteos tiene'))
                for i in range (allDairy):
                    try:
                        dairy=str(input("ingrese el nombre del lacteo:"))
                        cant=int(input("ingrese las cantidades de producto anterior: "))
                        listDairy.append(dairy)
                        listCantDairy.append(cant)
                        if i==allDairy-1:
                            bandera=False   
                 
                    except:
                            print("ingrese un tipo numerico")
                   
                self.dictDairy= dict(zip(listDairy,listCantDairy)) 
       
            except:
                print("ingrese un tipo numerico")
         
                

    def askGrain(self):
        listGrain=[]
        listCantGrain=[]
        bandera=TRUE
        while bandera:
            try:
                allGrain=int(input('cuantas clases de granos tiene'))
                for i in range (allGrain):
                    
                        try:
                             Grain=str(input("ingrese el nombre del grano:"))
                             cant=int(input("ingrese las cantidades de producto anterior: "))
                             listGrain.append(Grain)
                             listCantGrain.append(cant)
                             if i==allGrain-1:
                                 bandera=False 
                        except:
                            print("ingrese un tipo numerico")
                   
                self.dictGrain= dict(zip(listGrain,listCantGrain)) 
                
            except:
                print("ingrese un tipo numerico")
    
    def askCleaning(self):
        listCleaning=[]
        listCantCleaning=[]
        bandera = True
        while bandera:
            try:
                allcleaning=int(input('cuantas clases de Aseo tiene'))
                for i in range (allcleaning):
                    
                        try:
                             cleaning=str(input("ingrese el nombre del implemento de aseo:"))
                             cant=int(input("ingrese las cantidades de producto anterior: "))
                             listCleaning.append(cleaning)
                             listCantCleaning.append(cant)
                             if i==allcleaning-1:
                                 bandera=False 
                        except:
                            print("ingrese un tipo numerico")
                   
                self.dictCleaning= dict(zip(listCleaning,listCantCleaning)) 
                
            except:
                print("ingrese un tipo numerico")
    


 