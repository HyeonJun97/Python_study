#Q6.21

def sqrt(n):
    
    lastguess=1
    
    while True:
        nextguess=(lastguess+(n/lastguess))/2
        
        if nextguess-lastguess < 0.0001:
            return nextguess
            break
        lastguess= nextguess
        
def main():
    
    a=eval(input("제곱근을 구할 수를 입력하세요: "))
    
    print(a,"의 제곱근은", sqrt(a),"입니다.")

main()
