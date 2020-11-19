#Q5.53

import turtle
import math


turtle.penup()
turtle.goto(-200,0)
turtle.pendown()
turtle.goto(200,0)

turtle.setheading(150)
turtle.forward(20)
turtle.goto(200,0)
turtle.setheading(210)
turtle.forward(20) #축 화살표 그리기

turtle.penup()
turtle.goto(0,-80)
turtle.pendown()
turtle.goto(0,80)

turtle.setheading(240)
turtle.forward(20)
turtle.goto(0,80)
turtle.setheading(300)
turtle.forward(20)

turtle.penup()
turtle.goto(-100,-15)
turtle.pendown()
turtle.write("-2\u03c0")

turtle.penup()
turtle.goto(100,-15)
turtle.pendown()
turtle.write("2\u03c0")

turtle.penup()
turtle.color("red")
turtle.goto(-175,50*math.sin((-175/100)*2*math.pi))
turtle.pendown()
for x in range(-175, 176):
    turtle.goto(x,50*math.sin((x/100)*2*math.pi))

turtle.penup()
turtle.color("blue")
turtle.goto(-175,50*math.cos((-175/100)*2*math.pi))
turtle.pendown()
for x in range(-175, 176):
    turtle.goto(x,50*math.cos((x/100)*2*math.pi))
    
turtle.hideturtle()
turtle.done()
