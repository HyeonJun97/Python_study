# ex1
radius=20
area=radius*radius*3.14159
print("반지름이", radius,"인 원의 넓이는", area,"입니다.")

# ex2
radius = eval(input("반지름을 입력하세요: "))
area = radius*radius*3.14159
print("반지름이",radius,"인 원의 넓이는", area,"입니다.")

# ex3
number1=eval(input("첫 번째 숫자를 입력하세요: "))
number2=eval(input("두 번째 숫자를 입력하세요: "))
number3=eval(input("세 번째 숫자를 입력하세요: "))

average=(number1+number2+number3)/3

print(number1, number2, number3, "의 평균은", average, "입니다.")

# ex4
number1, number2, number3=eval(input("세 개의 숫자를 구분하여 입력하세요: "))
average=(number1+number2+number3)/3
print(number1, number2, number3, "의 평균은", average,"입니다.")

# ex5
seconds=eval(input("초 값을 정수로 입력하세요: "))
minute=seconds//60
remainseconds=seconds%60
print(seconds, "초는", minute, "분과", remainseconds, "초입니다.")

# ex6
purchaseamount=eval(input("총 구입액을 입력하세요: "))
tax=purchaseamount*0.06
print("판매세는", int(tax*100)/100.0,"입니다.")
