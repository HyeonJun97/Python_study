#Q6.4

def reverse(number):
    
    rnumber=0
    
    while number!=0:
        rnumber+=number%10
        rnumber*=10
        number=number//10
        
    rnumber=rnumber//10
    return rnumber

def main():
    
    number=eval(input("정수를 입력하세요: "))
    
    print(reverse(number))
    
main()