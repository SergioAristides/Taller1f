

from Puntoa import Supermarket


if __name__ == '__main__':
    supermarket= Supermarket("don Julio")
    while True:
        try:
            a=int(input("que categoria desea listar: \n ingrese 1 para la categoria de lacteos \n ingrese 2 par la categoria de granos \n e ingrese 3 para la categoria de aseo \n ingrese 4 para salir  "))
            if a==1:
                supermarket.askDairy()
                print(supermarket.dictDairy)
            if a==2:
                supermarket.askGrain()
                print(supermarket.dictGrain)
            if a==3:
                supermarket.askCleaning()
                print(supermarket.dictCleaning)
            if a==4:
                break
            
        except:
                print("ingrese un numero")
              
supermarket.imprimr()
    
       
    
    