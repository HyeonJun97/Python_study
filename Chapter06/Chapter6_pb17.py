#Q6.17

import math

def isValid(side1,side2,side3):
    
    if (side1+side2)>side3 and (side2+side3)>side1 and (side1+side3)> side2:
        return True
    else:
        return False
    
def area(side1,side2,side3):
    
    s=(side1+side2+side3)/2
    area=math.sqrt(s*(s-side1)*(s-side2)*(s-side3))
    
    return area

def main():
    
    s1,s2,s3=eval(input("세 변의 길이(실수)를 입력하세요: "))
    
    if isValid(s1,s2,s3) == True:
        print("삼각형의 넓이는", area(s1,s2,s3),"입니다.")
    else:
        print("잘못된 입력입니다.")

main()
