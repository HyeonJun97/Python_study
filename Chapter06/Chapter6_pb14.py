#Q6.14

def picheck(i):
    
    sum=0
    
    for a in range(1,i+1):
        sum+=(pow(-1,a+1)/(2*a-1))
    
    sum*=4
    
    return sum

def piprint(i):
    
    print(format(i,'3d'),"               ",format(picheck(i),'.4f'))

def main():
    
    print(" i                   m(i)")
    
    for i in range(1,1000,100):
        piprint(i)

main()