#Q6.27

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
    
    p1=2
    
    for i in range (3, 1001):
        if prime(i):
            if i-p1==2:
                print("(",p1,",",i,")")
            p1=i
            

main()