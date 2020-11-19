class LinearEquation:
    def __init__(self, a,b,c,d,e,f):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=d
        self.__e=e
        self.__f=f
    
    def geta(self):
        return self.__a
    def getb(self):
        return self.__b
    def getc(self):
        return self.__c
    def getd(self):
        return self.__d
    def gete(self):
        return self.__e
    def getf(self):
        return self.__f

    def isSolvable(self):
        if self.__a*self.__d-self.__b*self.__c==0:
            return False
        else:
            return True
    
    def getX(self):
        return (self.__e*self.__d-self.__b*self.__f)/(self.__a*self.__d-self.__b*self.__c)
    
    def getY(self):
        return (self.__a*self.__f-self.__e*self.__c)/(self.__a*self.__d-self.__b*self.__c)
    
def main():
    a,b,c,d,e,f=eval(input("a,b,c,d,e,f를 입력하세요: "))
    L=LinearEquation(a,b,c,d,e,f)
    
    if L.isSolvable():
        print("방정식의 해는",L.getX(),",",L.getY(),"입니다.")
    else:
        print("이 방정식의 해가 없습니다.")

main()

            