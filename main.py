

from Puntoa import Supermarket


if __name__ == '__main__':
    supermarket= Supermarket("don Julio")
    supermarket.askDairy()
    print(supermarket.dictDairy)
    supermarket.askGrain()
    print(supermarket.dictGrain)
    supermarket.askCleaning()
    print(supermarket.dictCleaning)
    
    