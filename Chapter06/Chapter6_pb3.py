#Q6.3

def reverse(number):
    
    rnumber=0
    
    while number!=0:
        rnumber+=number%10
        rnumber*=10
        number=number//10
        
    rnumber=rnumber//10
    return rnumber

def isPalindrome(number):
    if number==reverse(number):
        return True
    else:
        return False

def main():
    
    n=eval(input("정수를 입력하세요: "))
    
    if isPalindrome(n) == True:
        print(n,"은 대칭수입니다.")
    else:
        print(n,"은 대칭수가 아닙니다.")

main()