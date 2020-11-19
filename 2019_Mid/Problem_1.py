a,b,c=eval(input("세 개의 양의 정수를 입력하세요 : "))

sum=a+b+c

if sum%2==0:
    print("세 정수의 합은",sum)

else:
    max=a
    
    if b>max:
        max=b
    
    if c>max:
        max=c
    
    print("가장 큰 수는", max)
