
def main():
    s=input("숫자를 입력하세요: ")
    items=s.split()
    number=[eval(x) for x in items]
    
    reverse=[]
    
    for i in range(len(number)):
        n=number[i]
        reverse.insert(0,n)
        
    for i in range(len(number)):
        print(number[i], end=' ')
        
    print("")
        
    for i in range(len(reverse)):
        print(reverse[i], end=' ')

main()
