#Q5.41

a=eval(input("숫자를 입력하세요(0은 입력 종료):"))

if a==0:
    print("프로그램을 종료합니다.")

else:
    max=a
    count=1
    
    while a!=0:
        a=eval(input("숫자를 입력하세요(0은 입력 종료):"))
    
        if a>max:
            max=a
            count=1
        elif a==max:
            count+=1

    print("가장 큰 수는", max,"입니다.")
    print("가장 큰 수가 나타난 빈도수는", count,"번 입니다.")

    
    