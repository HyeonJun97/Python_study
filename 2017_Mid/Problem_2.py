import random

N = eval(input("0과 10사이 발생할 정수 개수를 입력하시오 : "))

max_val=0
max_count=1
min_val=10
min_count=1
mean=0
var=0
nsum=0
number2=0

for i in range (0,N):
    number=random.randint(0,10)
    print(number, end=" ")
    
    if number==max_val:
        max_count+=1
    
    if number>max_val:
        max_val=number
        max_count=1
    
    if number==min_val:
        min_count+=1
         
    if number<min_val:
        min_val=number
        min_count=1
    
    nsum+=number
    number2+=(number**2)

mean=nsum/N
number2/=N
var=round((number2-mean**2),2)

print("")    
print("가장 큰 수 : ", max_val, " 빈도수 : ", max_count)
print("가장 작은 수 : ", min_val, " 빈도수 : ", min_count)

print("발생된 수의 평균 :", mean, " 분산 : ", var )