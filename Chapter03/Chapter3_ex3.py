import turtle

turtle.pensize(3)
turtle.penup()
turtle.goto(-200,-50)
turtle.pendown()
turtle.begin_fill()
turtle.color("red")
turtle.circle(40,steps=3)
turtle.end_fill()

turtle.penup()
turtle.goto(-100,-50)
turtle.begin_fill()
turtle.color("blue")
turtle.circle(40,steps=4)
turtle.end_fill()

turtle.penup()
turtle.goto(200,-50)
turtle.pendown()
turtle.begin_fill()
turtle.color("purple")
turtle.circle(40)
turtle.end_fill()

turtle.color("green")
turtle.penup()
turtle.goto(-150,50)
turtle.pendown()
turtle.write("화려한 형형색색의 도형", font=("맑은 고딕", 18, "bold"))

turtle.hideturtle()

turtle.done()