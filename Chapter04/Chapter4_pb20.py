#Q4.20
y=eval(input("연도를 입력하세요(예.2008): "))
m=eval(input("월을 입력하세요(1-12): "))
q=eval(input("일을 입력하세요(1-31): "))

if m==1 or m==2:
    m+=12
    y-=1

j=y//100
k=y%100

h=(q+((26*(m+1))//10)+k+(k//4)+(j//4)+(5*j))%7

if h==0:
    print("요일은 토요일입니다.")
elif h==1:
    print("요일은 일요일입니다.")
elif h==2:
    print("요일은 월요일입니다.")
elif h==3:
    print("요일은 화요일입니다.")
elif h==4:
    print("요일은 수요일입니다.")
elif h==5:
    print("요일은 목요일입니다.")
elif h==6:
    print("요일은 금요일입니다.")