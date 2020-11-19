#Q4.1
import math

a, b, c=eval(input("a, b, c를 입력하세요: "))

d=pow(b,2)-4*a*c

if d>0:
    r1=(-b+math.sqrt(pow(b,2)-4*a*c))/2*a
    r2=(-b-math.sqrt(pow(b,2)-4*a*c))/2*a
    print("실근은", r1,"이고",r2,"입니다.")

elif d==0:
    r1=-b/(2*a)
    print("실근은", r1,"입니다.")

else:
    print("이 방정식의 실근이 존재하지 않습니다.")