#Q5.20

a=eval(input("패턴을 입력하세요(1~4): "))

if a==1:
    for i in range (0,6):
        for j in range (1, i+2):
            print(j,end=' ')
        print()

elif a==2:
    for i in range (0,6):
        for j in range (1,7-i):
            print(j,end=' ')
        print()

elif a==3:
    for i in range (0,6):
        for j in range (i, 6):
            print("  ",end='')
        for k in range (i+1,0,-1):
            print(k, end=' ')
        print()
        
elif a==4:
    for i in range (0,6):
        for j in range (6,i,-1):
            print(j,end=' ')
        print()
