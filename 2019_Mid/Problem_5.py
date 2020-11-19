x1,y1= eval(input("첫 번째 점에 대한 x1과 y1을 입력하세요: "))
x2,y2=eval(input("두 번째 점에 대한 x2과 y2을 입력하세요: "))

if x2-x1 ==0:
    print("직선의 방정식은 x=",x1)

else:
    m=(y2-y1)/(x2-x1)
    q=y1-m*x1
    print("직선의 방정식은 y=",m,"x+",q)
    