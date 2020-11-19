import math

class RegularPolygon:
    def __init__(self, n=3, side=1, x=0, y=0):
        self.__x=x
        self.__y=y
        self.__n=n
        self.__side=side
    
    def getx(self):
        return self.__x
    def gety(self):
        return self.__y
    def getn(self):
        return self.__n
    def getside(self):
        return self.__side
    
    def setx(self,x):
        self.__x=x
    def sety(self,y):
        self.__y=y
    def setn(self,n):
        self.__n=n
    def setside(self,side):
        self.__side=side
        
    def getPerimeter(self):
        return self.__side*self.__n
    
    def getArea(self):
        area=(self.__n*(self.__side**2))/(4*math.tan(math.pi/self.__n))
        return area
    
def main():
    r1=RegularPolygon()
    r2=RegularPolygon(6,4)
    r3=RegularPolygon(10,4,5.6,7.8)
    
    print("r1의 둘레:",r1.getPerimeter(),"r1의 넓이:", r1.getArea())
    print("r2의 둘레:",r2.getPerimeter(),"r2의 넓이:", r2.getArea())
    print("r3의 둘레:",r3.getPerimeter(),"r3의 넓이:", r3.getArea())
    
main()