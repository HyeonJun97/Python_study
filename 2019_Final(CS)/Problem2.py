# VectorCal 클래스 작성
class VectorCal:
    def __init__(self, vec1, vec2):
        self.v1=vec1
        self.v2=vec2
        
    def add(self):
        n=len(self.v1)
        add=[0]*n
        for i in range(n):
            add[i]=(self.v1[i]+self.v2[i])
        return add
    
    def sub(self):
        n=len(self.v1)
        sub=[0]*n
        for i in range(n):
            sub[i]=(self.v1[i]-self.v2[i])
        return sub
'''
class MoreVectorCal(VectorCal):
    def mul(self):        
        a=VectorCal()
        n=len(self.v1)
        mul=[0]*n
        for i in range(n):
            mul[i]=(self.v1[i]*self.v2[i])
        return mul
# MoreVectorCal 클래스를  VectorCal 클래스를 상속 받아 작성
'''

def main():
    
    x = [1, 2, 3]
    y = [-1, 1, 1]
#    a = MoreVectorCal(x, y)
    a=VectorCal(x,y)
    print("두 벡터의 합은 : ", a.add())
    print("두 벡터의 차는 : ", a.sub())
#    print("두 벡터의 곱은 : ", a.mul())
    
main()