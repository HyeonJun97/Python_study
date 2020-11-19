#Q2.26
import turtle
import math

x1, y1=eval(input("원의 중점을 입력하세요: "))
r=eval(input("반지름을 입력하세요: "))
area=round(r*r*math.pi,2)

turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.circle(r)

turtle.penup()
turtle.goto(x1,y1+r)
turtle.pendown()
turtle.write(area)

turtle.hideturtle()
turtle.done