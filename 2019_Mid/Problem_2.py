def gugu(x):
    for i in range (1,10):
        print(x,"*",i,"=",x*i)
        
def main():
    x=eval(input("구구단의 단을 입력하세요: "))
    gugu(x)
    
main()

