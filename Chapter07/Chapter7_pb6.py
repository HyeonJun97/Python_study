import math

class QuadraticEquation:
    def __init__(self, a, b, c):
        self.__a=a
        self.__b=b
        self.__c=c
    
    def geta(self):
        return self.__a
    def getb(self):
        return self.__b
    def getc(self):
        return self.__c
    
    def getDiscriminant(self):
        return self.__b**2-(4*self.__a*self.__c)
    
    def getRoot1(self):
        if self.getDiscriminant()<0:
            return 0
        else:
            return (-self.__b+math.sqrt(self.getDiscriminant()))/(2*self.__a)
    
    def getRoot2(self):
        if self.getDiscriminant()<0:
            return 0
        else:
            return (-self.__b-math.sqrt(self.getDiscriminant()))/(2*self.__a)
        
def main():
    a,b,c=eval(input("a,b,c값을 입력하세요: "))
    
    E=QuadraticEquation(a,b,c)
    
    if E.getDiscriminant()>0:
        print("방정식의 해는",E.getRoot1(),",",E.getRoot2(),"입니다.")
    
    elif E.getDiscriminant()==0:
        print("방정식의 해는",E.getRoot1(),"입니다.")
    
    else:
        print("이 방정식의 해가 없습니다.")

main()