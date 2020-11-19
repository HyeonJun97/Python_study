import random

X_INTERCEPT=200
Y_INTERCEPT=100
RAND_MAX=200
RAND_NUMBER=10

count_out = 0
count_in = 0


for i in range (0,RAND_NUMBER):
    x=random.random()*RAND_MAX
    y=random.random()*RAND_MAX
    
    if x<X_INTERCEPT and y<Y_INTERCEPT and y<-0.5*x+100:
        print("좌표 (",format(x,".2f"),",",format(y,".2f"),") 점은 삼각형의 내부에 있습니다.")
        count_in+=1
    else:
        print("좌표 (",format(x,".2f"),",",format(y,".2f"),") 점은 삼각형의 내부에 있지 않습니다.")
        count_out+=1

print("삼각형 내부 좌표 개수", count_in)
print("삼각형 외부 좌표 개수", count_out)

    
    