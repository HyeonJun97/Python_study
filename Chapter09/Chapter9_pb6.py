from tkinter import *
import random

class TTTP:
    def __init__(self):
        window=Tk()
        window.title("틱택토판")
        
        for i in range(3):
            for j in range(3):
                rnum=random.randint(0,1)
                if rnum==0:
                    self.rnumber=StringVar()
                    self.rnumber.set("O")
                    Label(window, textvariable=self.rnumber).grid(row=i,column=j)
                else:
                    self.rnumber=StringVar()
                    self.rnumber.set("X")
                    Label(window, textvariable=self.rnumber).grid(row=i,column=j)
    
    
        window.mainloop()
        

TTTP()