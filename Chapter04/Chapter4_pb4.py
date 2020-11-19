#Q4.4
import random

number1=random.randint(0,100)
number2=random.randint(0,100)

sum=number1+number2

answer=eval(input(str(number1)+"+"+str(number2)+"는 얼마입니까?"))

if answer==sum:
    print("정답입니다.")
else:
    print("틀렸습니다.","\n정답은", sum, "입니다.")