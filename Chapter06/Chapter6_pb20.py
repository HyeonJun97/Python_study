#Q6.20

import math

def distance(x1,y1,x2,y2):
    
    dist=math.sqrt(pow(x1-x2,2)+pow(y1-y2,2))
    
    return dist

def main():
    
    x1,y1,x2,y2=eval(input("두 점을 입력하세요: "))
    
    print("두 점사이의 거리는", distance(x1,y1,x2,y2),"입니다.")
    
main()
