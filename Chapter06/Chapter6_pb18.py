#Q6.18

import random

def printMatrix(n):
    
    for i in range(0,n):
        for j in range(0,n):
            a=random.randint(0,1)
            print(a,end=" ")
        print()

def main():
    
    n=eval(input("n을 입력하세요: "))
    
    printMatrix(n)
    
main()