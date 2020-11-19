
def main():
    s=input("10개의 숫자를 입력하세요: ")
    item=s.split()
    number=[eval(x) for x in item]
    
    e=eliminateDuplicate(number)
    
    print("중복을 제거한 고유한 숫자:", end=' ')
    
    for i in range(len(e)):
        print(e[i], end=' ')
    
def eliminateDuplicate(lst):
    new=[]
    
    for i in range(len(lst)):
        if lst[i] not in new:
            new.append(lst[i])
    
    return new

main()

        
        