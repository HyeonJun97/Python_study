#Q4.21

import math

x, y=eval(input("점의 두 좌표값을 입력하세요: "))

d=math.sqrt(pow(x,2)+pow(y,2))

if d<=10:
    print("점(",x,",",y,")은 원의 내부에 있습니다.")
else:
    print("점(",x,",",y,")은 원의 내부에 있지 않습니다.")