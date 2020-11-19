from tkinter import *

class tuza:
    def __init__(self):
        window =Tk()
        window.title("투자금 계산기")
        
        Label(window, text="투자금").grid(row=1,column=1,sticky=W)
        Label(window, text="기간").grid(row=2,column=1,sticky=W)
        Label(window, text="월이율").grid(row=3,column=1,sticky=W)
        Label(window, text="미래 가치").grid(row=4,column=1,sticky=W)

        self.tuzagm=StringVar()
        Entry(window, textvariable=self.tuzagm, justify=RIGHT).grid(row=1,column=2)
        self.gigan=StringVar()
        Entry(window, textvariable=self.gigan, justify=RIGHT).grid(row=2,column=2)
        self.monthrate=StringVar()
        Entry(window, textvariable=self.monthrate, justify=RIGHT).grid(row=3,column=2)        
        
        self.future=StringVar()
        Label(window, textvariable=self.future, justify=RIGHT).grid(row=4,column=2,sticky=E)
        
        Button(window, text="계산하기", command=self.compute).grid(row=5,column=2,sticky=E)

        window.mainloop()
    
    def compute(self):
        a=float(self.tuzagm.get())*((float(self.monthrate.get())/100+1)**(float(self.gigan.get())*12))
        self.future.set(format(a,".2f"))
tuza()