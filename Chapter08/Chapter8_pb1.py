
number=input("주민번호를 입력하세요: ").strip()

if len(number)!=14:
    print("주민번호가 올바르지 않습니다.")

else:
    for i in range(len(number)):
        test=True
        check=ord(number[i])
    
        if i==6:
            if check!=45:
                test=False
        else:
            if check<48 and check>57:
                test=False
            
            
    if test==True:
        print("올바른 주민번호입니다.")
    else:
        print("주민번호가 올바르지 않습니다.")


    
