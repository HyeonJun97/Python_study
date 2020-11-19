#Q5.16

n1 = eval(input("첫 번째 정수를 입력하세요: "))
n2 = eval(input("두 번째 정수를 입력하세요: "))

if n1>n2:
    d=n2
else:
    d=n1

for i in range(d,0,-1):
    if n1 % i==0 and n2 % i==0:
        gcd=i
        break

print(n1,"과",n2,"의 최대공약수는",gcd,"입니다.")