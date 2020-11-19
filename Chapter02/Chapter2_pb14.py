#Q2.14
import math
x1,y1,x2,y2,x3,y3=eval(input("삼각형의 세 꼭짓점을 입력하세요: "))

s1=math.sqrt(pow(x1-x2,2)+pow(y1-y2,2))
s2=math.sqrt(pow(x2-x3,2)+pow(y2-y3,2))
s3=math.sqrt(pow(x3-x1,2)+pow(y3-y1,2))

s=(s1+s2+s3)/2

area=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
area=round(area,1)

print("삼각형의 넓이는 ", area, "입니다.")