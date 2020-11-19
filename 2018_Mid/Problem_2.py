
while(True):
    x=eval(input("행의 개수를 입력하세요: "))
    if x>=1 and x<=10:
        for row in range(x,0,-1):
            for i in range(0,x-row):
                print("   ", end='')
                
            for j in range(row,0,-1):
                print(format(j,"2d"),end=' ')
                
            for k in range(j+1,row+1):
                print(format(k,"2d"), end=' ')
                
            print()
            
    else:
        print("1과 10 사이의 정수를 입력하세요.")
        print("프로그램을 종료합니다.")
        break
