import math

r=eval(input("중심에서 꼭짓점까지의 길이를 입력하세요: "))

s=2*r*math.sin(math.pi/5)

area=3*math.sqrt(3)/2*pow(s,2)

area=round(area, 2)

print("오각형의 넓이는", area , "입니다.")