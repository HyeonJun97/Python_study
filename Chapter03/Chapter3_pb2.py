import math

x1, y1=eval(input("첫 번째 점(위도와 경도)을 60분법 각으로 입력하세요: "))
x2, y2=eval(input("두 번째 점(위도와 경도)을 60분법 각으로 입력하세요: "))

x1=math.radians(x1)
x2=math.radians(x2)
y1=math.radians(y1)
y2=math.radians(y2)

r=6370.01
d=r*math.acos(math.sin(x1)*math.sin(x2)+math.cos(x1)*math.cos(x2)*math.cos(y1-y2))

print("두 점 사이의 거리는", d, "km입니다.")