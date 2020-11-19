
def reverse1():
    number=eval(input("네 자리 정수를 입력하세요: "))
    
    digit1=str(number//1000)
    number%=1000
    digit2=str(number//100)
    number%=100
    digit3=str(number//10)
    number%=10
    digit4=str(number)
    
    rnumber=digit4+digit3+digit2+digit1
    
    print("정수 역순은",rnumber,"입니다.")
    
def reverse2(number):
    rnumber2=""
    while(number>0):
        rnumber2+=str(number%10)
        number//=10
    
    print("정수 역순은",rnumber2,"입니다.")
    
def reverse3(number):
    reverseNumber=0
    while(number>0):
        reverseNumber*=10
        reverseNumber+=number%10
        number//=10
    
    return reverseNumber

def main():
    
    reverse1()
    print()
    
    number=eval(input("정수를 입력하세요: "))
    reverse2(number)
    print()
    
    number=eval(input("정수를 입력하세요: "))
    reverseNumber=reverse3(number)
    print("정수 역순은",reverseNumber,"입니다.")
    
main()