#Q5.2
import random
import time

acount=0
count=0
a=15

starttime=time.time()

while count<a:
    number1=random.randint(1,15)
    number2=random.randint(1,15)
    
    answer=eval(input(str(number1)+"+"+str(number2)+"는 얼마입니까?"))
    
    if number1+number2==answer:
        print("정답입니다!")
        acount+=1
    else:
        print("틀렸습니다.\n정답은" ,number1+number2,"입니다.")
    
    count+=1

print()
endtime=time.time()
testtime=int(endtime-starttime)
print("정답의 개수는", a,"개 중",acount,"개입니다.\n수행시간은",testtime,"초입니다.")