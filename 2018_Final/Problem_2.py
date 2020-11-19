from tkinter import * # Import tkinter
    
class DotProductGUI:
    
    def computedotProduct(self):
        s1=str(self.vector1.get())
        i1=s1.split()
        v1=[eval(x) for x in i1]
        s2=str(self.vector2.get())
        i2=s2.split()
        v2=[eval(x) for x in i2]

        if len(v1) != len(v2):
            self.dot.set("벡터길이가 다름!")
        else:
            dot=0
            for i in range(len(v1)):
                dot+=(v1[i]*v2[i])
            self.dot.set(dot)

    def __init__(self):
        window = Tk() # Create a window
        window.title("벡터 내적 계산") # Set title
        
        Label(window, text="벡터 1").grid(row=1,column=1,sticky=W)
        Label(window, text="벡터 2").grid(row=2,column=1,sticky=W)
        Label(window, text="내적").grid(row=3,column=1,sticky=W)
        
        self.dot=StringVar()
        Label(window, textvariable=self.dot).grid(row=3,column=2,sticky=E)
        
        self.vector1=StringVar()
        Entry(window,textvariable=self.vector1, justify=LEFT).grid(row=1,column=2)
        self.vector2=StringVar()
        Entry(window,textvariable=self.vector2, justify=LEFT).grid(row=2,column=2)
        
        Button(window, text = "계산", command = self.computedotProduct).grid(row = 4, column = 2, sticky = E)
        
        window.mainloop() # Create an event loop

DotProductGUI()