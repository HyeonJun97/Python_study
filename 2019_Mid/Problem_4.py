high= eval(input("공의 높이를 입력하세요: "))
count=0

high/=2

while high>0.01:
    count+=1
    high/=2
    
print("공이 튀긴 횟수는",count,"회입니다.")