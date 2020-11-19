from tkinter import *

class RECT:
    def __init__(self):
        window=Tk()
        window.title("직사각형 출력하기")
        
        self.canvas=Canvas(window, width=400, height=200, bg="white")
        self.canvas.pack()
        
        for i in range(20):
            self.canvas.create_rectangle(100-5*i,100-5*i,300+5*i,100+5*i)
        
        window.mainloop()
        
RECT()