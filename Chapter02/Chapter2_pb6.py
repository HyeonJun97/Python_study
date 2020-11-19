#Q2.6
a=eval(input("0~1000사이의 정수를 입력하세요: "))

sum=a%10
a=a//10
sum+=a%10
a=a//10
sum+=a%10

print("각 자릿수의 합은", sum, "입니다.")