#Q5.1

pnum=0
mnum=0
sum=0
avg=0
count=0
number=-1

while number != 0:
    number=eval(input("정수를 입력하세요. 입력값이 0이면 종료됩니다: "))
    if number==0 and count==0:
        print("아무 숫자도 입력하지 않았습니다.")
        break
    elif number==0 and count!=0:
        print("양수의 개수는", pnum, "개입니다.")
        print("음수의 개수는", mnum, "개입니다.")
        print("총합은", sum, "입니다.")
        print("평균은", avg, "입니다.")
    elif number>0:
        pnum+=1
    elif number<0:
        mnum+=1

    sum+=number
    avg=sum/(pnum+mnum)
    count+=1

