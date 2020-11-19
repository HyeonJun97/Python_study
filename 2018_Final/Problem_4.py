from GeometricObject import GeometricObject
import math

class Triangle(GeometricObject):
    def __init__(self, side):
        super().__init__()
        self.__side=side
    
    def getSide(self):
        return self.__side
    
    def getArea(self):
        area=(math.sqrt(3)*pow(self.__side,2)/4)
        return area
    
    def getPerimeter(self):
        return self.__side*3
    
    def __str__(self):
        return "<정삼각형> " + super().__str__() + " 한변 길이 : " + str(self.getSide()) + " 면적 : " + str(self.getArea()) + " 둘레 : " + str(self.getPerimeter())

class Rectangle(GeometricObject):
    def __init__(self, side):
        super().__init__()
        self.__side=side
    
    def getSide(self):
        return self.__side
    
    def getArea(self):
        area=pow(self.__side,2)
        return area
    
    def getPerimeter(self):
        return self.__side*4
    
    def __str__(self):
        return "<정사각형> " + super().__str__() + " 한변 길이 : " + str(self.getSide()) + " 면적 : " + str(self.getArea()) + " 둘레 : " + str(self.getPerimeter())
    
def setFilledObject(g, filled):
    if filled == 1:
        g.setFilled=True
    else:
        g.setFilled=False
        

def displayObject(g):
    print(g.__str__())

def isSamePerimeter(g1, g2):
    p1=g1.getPerimeter()
    p2=g2.getPerimeter()
    
    if p1==p2:
        return True
    else:
        return False

 
def main():
    tri_side = eval(input("정삼각형의 한 변의 길이를 입력하시오 : "))
    triangle = Triangle(tri_side);
    
    color = input("정삼각형의 색깔을 입력하시오 : ")
    triangle.setColor(color);
    
    filled = eval(input("내부를 채우기 1, 그렇지 않으면 0을 입력하시오. : "))
    setFilledObject(triangle, filled)

    print()
    
    rec_side = eval(input("정사각형의 한 변의 길이를 입력하시오 : "))
    rectangle = Rectangle(rec_side);
    
    color = input("정사각형의 색깔을 입력하시오 : ")
    rectangle.setColor(color);
    
    filled = eval(input("내부를 채우기 1, 그렇지 않으면 0을 입력하시오. : "))
    setFilledObject(rectangle, filled)
    
    print()
    displayObject(triangle)
    displayObject(rectangle)
    
    print()
    print("정삼각형과 정사각형의 둘레는 같습니까 ? : ", isSamePerimeter(triangle, rectangle))

    
main()