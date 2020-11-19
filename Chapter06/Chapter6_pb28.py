#Q6.28

import random

def craps():
    
    n1=random.randint(1,6)
    n2=random.randint(1,6)
    
    sum=n1+n2
    
    if sum==2 or sum==3 or sum==12:
        print("주사위",n1,"+",n2,"=",sum,"이/가 나왔습니다.")
        print("당신이 졌습니다.")
    
    elif sum==7 or sum==11:
        print("주사위",n1,"+",n2,"=",sum,"이/가 나왔습니다.")
        print("당신이 이겼습니다.")
        
    else:
        print("주사위",n1,"+",n2,"=",sum,"이/가 나왔습니다.")
        print(sum,"점입니다.")
        while True:
            n1=random.randint(1,6)
            n2=random.randint(1,6)
            
            newsum=n1+n2
            
            if newsum==sum:
                print("주사위",n1,"+",n2,"=",newsum,"이/가 나왔습니다.")
                print("당신이 이겼습니다.")
                break
            elif newsum==7:
                print("주사위",n1,"+",n2,"=",newsum,"이/가 나왔습니다.")
                print("당신이 졌습니다.")
                break

def main():
    
    craps()
    
main()
    