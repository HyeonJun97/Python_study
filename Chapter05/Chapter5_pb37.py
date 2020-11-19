#Q5.37

import math

sum=0

for i in range (1,625):
    sum+=(1/(i+math.sqrt(i+1)))
    
print("합계는", sum,"입니다.")