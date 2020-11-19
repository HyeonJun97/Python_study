from GeometricObject import GeometricObject

class Triangle(GeometricObject):
    def __init__(self, side1=1.0,side2=1.0,side3=1.0):
        super().__init__()
        self.side1=side1
        self.side2=side2
        self.side3=side3
    
    def getside1(self):
        return self.side1
    def setside1(self,side1):
        self.side1=side1
    def getside2(self):
        return self.side1
    def setside2(self,side2):
        self.side2=side2
    def getside3(self):
        return self.side1
    def setside3(self,side3):
        self.side3=side3

    def getArea(self):
        s=(self.side1+self.side2+self.side3)/2
        area=(s*(s-self.side1)*(s-self.side2)*(s-self.side3))**0.5
        return area
    
    def getPerimeter(self):
        return self.side1+self.side2+self.side3
    
    def __str__(self):
        return "Triangle: side1 =" + str(self.side1) + " side2 = " + str(self.side2) + " side3 = " + str(self.side3)

    def tprint(self):
        print(self.__str__())
        
def main():
    s1,s2,s3=eval(input("삼각형의 세변의 길이를 입력하세요: "))
    p=eval(input("삼각형의 색칠(1-색칠,0-비움): "))
    
    t=Triangle(s1,s2,s3)
    
    if p==1:
        t.setFilled(True)
    elif p==0:
        t.setFilled(False)
    
    print("넓이 : ", t.getArea())
    print("둘레 : ", t.getPerimeter())
    print("채움 : ", t.isFilled())
    t.tprint()
    
main()