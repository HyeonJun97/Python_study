
def main():
    s=input("10개의 정수를 입력하세요: ")
    item=s.split()
    number=[eval(x) for x in item]
    
    a=eliminateDuplicate(number)
    b=a
    count=1
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]<=b[j]:
                if count%5==0:
                    print("(",a[i],",",b[j],")")
                else:
                    print("(",a[i],",",b[j],")", end=' ')
                count+=1


def eliminateDuplicate(lst):
    new=[]
    
    for i in range(len(lst)):
        if lst[i] not in new:
            new.append(lst[i])
    
    return new

main()
