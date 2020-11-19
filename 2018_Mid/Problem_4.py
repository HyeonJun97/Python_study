import random
import turtle

DOT_SIZE=5          # 좌표 점의 크기
DOT_COLOR="red"    # 좌표 점의 색깔
LINE_COLOR="blue"   # 직선의 색깔

def getPoints(side):
    x=random.randint(-side,side)
    return x

def computeDistance(x,y):
    dist=(x**2+y**2)**0.5
    return dist

def drawCircle(x=0,y=0,radius=10):
    turtle.penup()
    turtle.goto(x,y-radius)
    turtle.pendown()
    turtle.circle(radius)

def drawRectangle(x=0,y=0,width=20,height=20):
    turtle.penup()
    turtle.goto(x-width/2,y+height/2)
    turtle.pendown()
    turtle.goto(x+width/2,y+height/2)
    turtle.goto(x+width/2,y-height/2)
    turtle.goto(x-width/2,y-height/2)
    turtle.goto(x-width/2,y+height/2)
    

def drawCenter(x=0,y=0):

    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.dot(DOT_SIZE,DOT_COLOR)
    a="("+str(x)+","+str(y)+")"
    turtle.color(LINE_COLOR)
    turtle.write(a)
    
def drawLine(x,y,distance):

    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.color(LINE_COLOR)
    turtle.goto(x,y)
    turtle.penup()
    turtle.goto(x/2,y/2)
    turtle.pendown()
    distance=str(format(distance,".2f"))
    turtle.write(distance)

def main():
    radius, numberOfPoints=eval(input("원의 반지름과 생성할 점의 개수를 입력하세요: "))
    nearx,neary,neardis=radius, radius, computeDistance(radius,radius)
    farx,fary,fardis=0, 0, 0
    for i in range(0, numberOfPoints):
        x=getPoints(radius)
        y=getPoints(radius)
        point="("+str(x)+","+str(y)+")"
        print(point,end=" ")
        distance=computeDistance(x,y)
        
        if distance>farx:
            farx=x
            fary=y
            fardis=distance
        
        if distance<neardis:
            nearx=x
            neary=y
            neardis=distance
    
    nearpoint="("+str(nearx)+","+str(neary)+")"    
    farpoint="("+str(farx)+","+str(fary)+")"
    print("")
    print("nearest points:",nearpoint)
    print("nearest distance:", neardis)
    print("far points:",farpoint)
    print("far distance:", fardis)
        
    drawCircle(0,0,radius)
    drawRectangle(0,0,radius*2,radius*2)
    
    drawCenter(0,0)
    
    drawCenter(nearx,neary)
    drawLine(nearx,neary,neardis)
    
    drawCenter(farx,fary)
    drawLine(farx,fary,fardis)
    
    turtle.done()
    
    
main()