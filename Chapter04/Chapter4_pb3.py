#Q4.3

a, b, c, d, e, f=eval(input("a, b, c, d, e, f를 입력하세요: "))

if (a*d-b*c) == 0:
    print("이 방정식은 해가 없습니다.")
else:
    x=(e*d-b*f)/(a*d-b*c)
    y=(a*f-e*c)/(a*d-b*c)
    print("x는", x,"이고 y는",y,"입니다.")
