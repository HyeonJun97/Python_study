import math

def sidelength(A,B,c):
    A=(math.pi/180)*A
    B=(math.pi/180)*B
    C=math.pi-A-B
    return (c*math.sin(A))/math.sin(C)
    
def main():
    A, B, c= eval(input("각도 A, B와 변 c의 길이를 입력: "))
    print("선분 a(BC)의 길이는", sidelength(A,B,c))
main()