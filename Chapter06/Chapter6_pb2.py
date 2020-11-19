#Q6.2

def sumDigits(n):
    sum=0
    while n!=0:
        sum+=n%10
        n=n//10
    return sum
    

def main():
    a=eval(input("정수를 입력하세요: "))
    print(a,"의 각 자릿수의 합은",sumDigits(a),"입니다.")
    
main()