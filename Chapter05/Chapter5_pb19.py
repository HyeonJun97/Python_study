#Q5.19

number=eval(input("행의 개수를 입력하세요: "))

for i in range(1,number+1):
    a=i
    
    for j in range(i,number):
        print(" ", end="  ")
    
    for k in range(0,i):
        print(format(a, '2d'), end=' ')
        a-=1
    
    a+=2
    
    for q in range(0,i-1):
        print(format(a, '2d'), end=' ')
        a+=1
    
    print()
