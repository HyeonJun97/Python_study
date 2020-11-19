#Q5.34

import random

lottery1=random.randint(1,9)
lottery2=random.randint(1,9)

if lottery1==lottery2:
    check=0
else:
    check=1

while check==0:
    if lottery1==lottery2:
        lottery2=random.randint(1,9)
    else:
        check=1

lottery1*=10
lottery=lottery1+lottery2

print("복권당첨번호는",lottery,"입니다.")
