#Q4.37

import turtle

x1, y1, w1, h1=eval(input("중점좌표와 폭과 높이를 입력하세요: "))
x2, y2, w2, h2=eval(input("중점좌표와 폭과 높이를 입력하세요: "))

turtle.penup()
turtle.goto(x1-w1/2,y1-h1/2)
turtle.pendown()
turtle.goto(x1+w1/2,y1-h1/2)
turtle.goto(x1+w1/2,y1+h1/2)
turtle.goto(x1-w1/2,y1+h1/2)
turtle.goto(x1-w1/2,y1-h1/2)

turtle.penup()
turtle.goto(x2-w2/2,y2-h2/2)
turtle.pendown()
turtle.goto(x2+w2/2,y2-h2/2)
turtle.goto(x2+w2/2,y2+h2/2)
turtle.goto(x2-w2/2,y2+h2/2)
turtle.goto(x2-w2/2,y2-h2/2)

turtle.penup()
turtle.goto(0,-200)

if (x1-w1/2<=x2-w2/2<=x1+w1/2) and (x1-w1/2<=x2+w2/2<=x1+w1/2) and (y1-h1/2<=y2+h2/2<=y1+h1/2) and (y1-h1/2<= y2+h2/2<= y1+h1/2):
    turtle.write("r2는 r1와 내부에 있습니다.")
elif (x2-w2/2<=x1-w1/2<=x2+w2/2) and (x2-w2/2<=x1+w1/2<=x2+w2/2) and (y2-h2/2<=y1+h1/2<=y2+h2/2) and (y2-h2/2<= y1+h1/2<= y2+h2/2):
    turtle.write("r1는 r2와 내부에 있습니다.")
elif (x1+w1/2<x2-w2/2) or (x2+w2/2 < x1-w1/2) or (y1+h1/2<y2-h2/2) or (y2+h2/2<y1-h1/2):
    turtle.write("r2는 r1과 겹치지 않습니다.")
else:
    turtle.write("r2는 r1과 겹칩니다.")
    
turtle.done()