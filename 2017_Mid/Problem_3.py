import math

def main():
    
    x1, y1 = eval(input("첫 번째 점에 대한 x1과 y1을 입력하세요: "))    
    x2, y2 = eval(input("두 번째 점에 대한 x2와 y2를 입력하세요: "))   
    x3, y3 = eval(input("세 번째 점에 대한 x3와 y3를 입력하세요: "))
    
    dist1=distance(x1,y1,x2,y2)
    dist2=distance(x2,y2,x3,y3)
    dist3=distance(x3,y3,x1,y1)
    
    dist1,dist2,dist3=sortedNumbers(dist1,dist2,dist3)
    
    area=getTriArea(dist1,dist2,dist3)
    
    print("삼각형의 세점은 :", "(",x1,y1,")", "(",x2,y2,")", "(",x3,y3,")" )
    print("세점 사이의 거리는 : ", dist1, dist2, dist3)
    print("세점에 의한 삼각형의 면적은 : ", area)

    
def distance(x1,y1,x2,y2):
    return math.sqrt(pow(x1-x2,2)+pow(y1-y2,2))

def sortedNumbers(dist1,dist2,dist3):
    if dist1>dist2:
        temp=dist1
        dist1=dist2
        dist2=temp
    
    if dist1>dist3:
        temp=dist1
        dist1=dist3
        dist3=temp
    
    if dist2>dist3:
        temp=dist2
        dist2=dist3
        dist3=temp
    
    return dist1,dist2,dist3
   
def getTriArea(a,b,c):
    s=(a+b+c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))
    
main()