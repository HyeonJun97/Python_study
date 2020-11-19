#Q3.10
n=eval(input("정수를 입력하세요:"))

ivn=0

ivn+=n//1000
n%=1000

ivn+=n//100*10
n%=100

ivn+=n//10*100
n%=10

ivn+=n*1000

print("숫자 역순은",ivn,"입니다.")

