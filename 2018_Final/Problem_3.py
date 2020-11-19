import random

class squareMatrix:
    
    def __init__(self, n):
        self.dim=n
        self.mat=[]
        self.initMatrix()
        
    def initMatrix(self):
        for row in range(self.dim):
            self.mat.append([])
            for column in range(self.dim):
                self.mat[row].append(0)
        
    def genMatrix(self):
        newmat=[]
        for row in range(self.dim):
            newmat.append([])
            for column in range(self.dim):
                newmat[row].append(random.randint(0,1))
        self.mat=newmat
        
    def printMatrix(self, s):
        print(s)
        for row in range(self.dim):
            for column in range(self.dim):
                print(self.mat[row][column], end=' ')
            print("")
        
def MatrixAND(m1, m2):
    andmat=squareMatrix(m1.dim)
    
    for i in range(m1.dim):
        for j in range(m1.dim):
            if m1.mat[i][j]==1 and m2.mat[i][j]==1:
                andmat.mat[i][j]=1
                
    return andmat

def MatrixMult(m1, m2):
    mulmat=squareMatrix(m1.dim)
    
    for i in range(m1.dim):
        for j in range(m1.dim):
            a=m1.mat[i][j]*m2.mat[i][j]
            mulmat.mat[i][j]=a
            
    return mulmat

def main():
    n = eval(input("정사각형 행렬의 크기를 입력하시오. : "))
    
    m1 = squareMatrix(n)
    m1.genMatrix()
    m1.printMatrix("m1 = ")

    m2 = squareMatrix(n)   
    m2.genMatrix()
    m2.printMatrix("m2 = ")

    m3 = MatrixMult(m1, m2)
    m3.printMatrix("m1 * m2  = ")
    
    m4 = MatrixAND(m1, m2)
    m4.printMatrix("m1 and m2 = ")
    
main()