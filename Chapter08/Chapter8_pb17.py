class Point:
    def __init__(self, x=0, y=0):
        self.__x=x
        self.__y=y
    
    def getx(self):
        return self.__x
    def gety(self):
        return self.__y
    
    def distance(self, p):
        x1=p.getx()
        y1=p.gety()
        return ((x1-self.__x)**2+(y1-self.__y)**2)**0.5
    
    def isNearBy(self, p):
        if self.distance(p)<=5:
            return True
        else:
            return False
        
    def __str__(self):
        x=str(self.__x)
        y=str(self.__y)
        return "("+x+","+y+")"
        
def main():
    x1,y1,x2,y2=eval(input("두 점 x1,y1,x2,y2를 입력하세요: "))
    
    p1=Point(x1,y1)
    p2=Point(x2,y2)
    
    dist=p1.distance(p2)
    print("두 점 사이의 거리는", format(dist,".2f"),"입니다.")
    
    if p1.isNearBy(p2):
        print("두 점은 서로 가까이에 있습니다.")
    else:
        print("두 점은 서로 가까이에 있지 않습니다.")
    
main()