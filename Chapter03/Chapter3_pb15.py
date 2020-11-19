#Q3.15
import turtle

turtle.penup()
turtle.goto(-400,0)
turtle.pendown()
for i in range(1,4):
    turtle.forward(120)
    turtle.left(120)

turtle.penup()
turtle.goto(-200,0)
turtle.pendown()
for i in range(1,5):
    turtle.forward(100)
    turtle.left(90)


turtle.penup()
turtle.goto(0,0)
turtle.pendown()
for i in range(1,6):
    turtle.forward(80)
    turtle.left(72)

turtle.penup()
turtle.goto(200,0)
turtle.pendown()
for i in range(1,7):
    turtle.forward(70)
    turtle.left(60)


turtle.penup()
turtle.goto(400,0)
turtle.pendown()
for i in range(1,9):
    turtle.forward(50)
    turtle.left(45)

turtle.done()
