class Rectangle:
    def __init__(self, width=1, height=2):
        self.width=width
        self.height=height
    
    def getArea(self):
        return self.width*self.height
    
    def getPerimeter(self):
        return 2*(self.width+self.height)
    
def main():
    r1=Rectangle(4,10)
    r2=Rectangle(3.5,35.7)
    
    print("폭:",r1.width,"높이:",r1.height,"넓이:",r1.getArea(),"둘레:",r1.getPerimeter())
    print("폭:",r2.width,"높이:",r2.height,"넓이:",r2.getArea(),"둘레:",r2.getPerimeter())
    
main()