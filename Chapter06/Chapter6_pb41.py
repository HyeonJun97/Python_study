#Q6.41

import turtle
import random
import math
#from UsefulturtleFunction import *       6.14코드 함수들

def drawPoint(x, y):
    turtle.penup() # 펜을 위로 들어 올린다.
    turtle.goto(x, y)
    turtle.pendown() # 펜을 아래로 내린다.
    turtle.begin_fill() # 도형을 색깔로 채우기 시작한다.
    turtle.circle(3)
    turtle.end_fill() # 도형을 색깔로 채운다.


def drawCircle(x, y, radius):
    turtle.penup() # 펜을 위로 들어 올린다.
    turtle.goto(x, y - radius)
    turtle.pendown() # 펜을 아래로 내린다.
    turtle.circle(radius)


def drawRectangle(x, y, width, height):
    turtle.penup() # 펜을 위로 들어 올린다.
    turtle.goto(x + width / 2, y + height / 2)
    turtle.pendown() # 펜을 아래로 내린다.
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    
    
def main():
    
    drawRectangle(-75,0,100,100)
    drawCircle(50,0,50)
    
    for i in range(0,10):
        x1=random.randint(-125,-25)
        y1=random.randint(-50,50)
        drawPoint(x1,y1)
    for j in range(0,10):
        x2=random.randint(25,100)
        y2=random.random()*2*math.sqrt(50**2-(x2-50)**2)-math.sqrt(50**2-(x2-50)**2)
        drawPoint(x2,y2)
        
    turtle.hideturtle()
    turtle.done()

main()