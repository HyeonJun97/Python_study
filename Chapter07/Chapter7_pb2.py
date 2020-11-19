class Stock:
    def __init__(self, symbol, name, previousPrice, currentPrice):
        self.__symbol=symbol
        self.__name=name
        self.__previousPrice=previousPrice
        self.__currentPrice=currentPrice
        
    def getsymbol(self):
        return self.__symbol
    
    def getname(self):
        return self.__name
    
    def getpreviousPrice(self):
        return self.__previousPrice
    
    def getcurrentPrice(self):
        return self.currentPrice
    
    def setpreviousPrice(self, previousPrice):
        self.__previousPrice=previousPrice
    
    def setcurrentPrice(self, currentPrice):
        self.__currentPrice=currentPrice
    
    def getChangePercent(self):
        return format((self.__currentPrice - self.__previousPrice) * 100 / self.__previousPrice, ".2f")

def main():
    
    s=Stock('INTC','Intel Corporation',20500,20350)
    
    print("가격변동률:", str(s.getChangePercent()), "%")

main()
