import turtle

x1, y1=eval(input("x1, y1을 입력하세요: "))
x2, y2=eval(input("x2, y2을 입력하세요: "))

distance=((x1-x2)**2+(y1-y2)**2)**0.5

turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.write("점1")
turtle.goto(x2,y2)
turtle.write("점2")

turtle.penup()
turtle.goto((x1+x2)/2,(y1+y2)/2)
turtle.write(distance)

turtle.done()