#Q5.40

import random

hcount=0
tcount=0

for i in range(1000000):
    coin=random.randint(0,1)
    if coin == 0:
        hcount+=1
    else:
        tcount+=1
        
print("동전의 앞면이 나온 횟수:",hcount)
print("동전의 뒷면이 나온 횟수:",tcount)
