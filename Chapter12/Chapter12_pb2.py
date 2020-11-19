class Location():
    def __init__(self, row, column, maxvalue):
        self.row=row
        self.column=column
        self.maxvalue=maxvalue
        
    def getrow(self):
        return self.row
    
    def getcolumn(self):
        return self.column
    
    def getmaxvalue(self):
        return self.maxvalue
    
    def setrow(self, row):
        self.row=row
    
    def setcolumn(self, column):
        self.column=column
        
    def setmaxvalue(self, maxvalue):
        self.maxvalue=maxvalue
            
def locateLargest(a):
    large=Location(0,0,a[0][0])
    
    for row in range(len(a)):
        for col in range(len(a[row])):
            if a[row][col] > large.getmaxvalue():
                large.setrow(row)
                large.setcolumn(col)
                large.setmaxvalue(a[row][col])
    
    return large

def main():
    r,c=eval(input("리스트의 행과 열의 개수를 입력하시오 : "))
    
    matrix=[]
    
    for i in range(r):
        matrix.append([])
        ss=str(i)+"번 행을 입력하시오: "
        s=input(ss)
        item=s.split()
        matrix[i]=[eval(x) for x in item]
    
    lmax=locateLargest(matrix)
    
    print("최대값 원소의 위치는 (", lmax.getrow(),",",lmax.getcolumn(),")이고 최댓값은",lmax.getmaxvalue(),"입니다.")
    
main()