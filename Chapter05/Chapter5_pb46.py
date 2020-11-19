#Q5.46

import math

x=eval(input("10개의 숫자를 입력하세요: "))

n=10
xsum=x
dxsum=pow(x,2)
avg=0
std=0

for i in range (0,9):
    x=eval(input(""))
    xsum+=x
    dxsum+=pow(x,2)

avg=xsum/n

std=math.sqrt((dxsum-(pow(xsum,2)/n))/(n-1))


print("평균은", format(avg,".2f"), "입니다.")
print("표준 편차는", format(std,".5f"), "입니다.")
