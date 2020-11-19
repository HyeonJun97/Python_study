class Account:
    def __init__(self, iid=0, balance=100000, annualrate=0):
        self.__iid=iid
        self.__balance=balance
        self.__annualrate=annualrate
    
    def getiid(self):
        return self.__iid
    def getbalance(self):
        return self.__balance
    def getannualrate(self):
        return self.__annualrate
    
    def setiid(self,iid):
        self.__iid=iid
    def setbalance(self, balance):
        self.__balance=balance
    def setannualrate(self, annualrate):
        self.__annualrate=annualrate
    
    def getmonthlyrate(self):
        return self.__annualrate/12
    def getmonthlyinterest(self):
        return self.__balance*self.getmonthlyrate()/100
    
    def withdraw(self,a):
        self.__balance-=a
    def deposit(self,b):
        self.__balance+=b
'''
class ATM(Account):
    def __init__(self):
        super().__init__()
        Account(0)=

def main():
    
main()'''