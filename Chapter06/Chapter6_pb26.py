#Q6.26

def prime(n):
    
    count=0
    
    for i in range (2, n+1):
        if n%i== 0:
            count+=1
        
        if count==2:
            break

    if count==1:
        return True
    else:
        return False
    
def main():
    print(" p          2^p - 1")
    
    for p in range(2, 32):
        mer=pow(2,p)-1
        if prime(mer):
            print(format(p,'2d'),format(mer,'15d'))

main()