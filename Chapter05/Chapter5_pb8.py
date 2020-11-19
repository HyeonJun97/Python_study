#Q5.8

import math

print("숫자        제곱근")

for a in range(0,21,2):
    if a<10:
        print(a,"         ", format(math.sqrt(a),".4f"))
    else:
        print(a,"        ", format(math.sqrt(a),".4f"))  