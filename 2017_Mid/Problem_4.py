import turtle

class Square:
    def __init__(self,length=100):
        self.length=length
    
    def getArea(self):
        return self.length**2
    
    def getPerimeter(self):
        return self.length*4

def main():
    
    length = eval(input("정사각형의 한 변의 길이를 입력하시오 : "))
        
    s1=Square(length)
    area=s1.getArea()
    perimeter=s1.getPerimeter()
    
    print("정사각형의 길이: ", length,  "면적 : ", area, "둘레 : ", perimeter)
    
    message="면적:"+str(area)
    
    turtle.pensize(3)
    turtle.penup()
    turtle.goto(0,length/(2**0.5))
    turtle.pendown()
    turtle.goto(length/(2**0.5),0)
    turtle.goto(0,-length/(2**0.5))
    turtle.goto(-length/(2**0.5),0)
    turtle.goto(0,length/(2**0.5))
    turtle.penup()
    turtle.goto(-30,-length/(2**0.5)-30)
    turtle.pendown()
    turtle.write(message, font=("Arial",10,"bold"))
    turtle.hideturtle()
    turtle.done()
    
main()