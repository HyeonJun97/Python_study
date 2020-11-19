#Q6.12

def printchars(ch1,ch2,npl):
    
    n1=ord(ch1)
    n2=ord(ch2)
    count=0
    
    for i in range(n1, n2+1):
       print(chr(i),end=' ')
       count=count+1
       
       if count==npl:
           print()
           count=0

def main():
    print(printchars("1","Z",10))

main()