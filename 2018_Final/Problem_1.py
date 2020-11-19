import math

def indexOfSmallestElement(x):
    idx=0
    nmin=10
    for i in range(len(x)):
        if nmin>x[i]:
            nmin=x[i]
            idx=i
    return idx, nmin

def mean(x):
    sum=0
    for i in range(len(x)):
        sum+=x[i]
    
    return sum/(len(x))

def deviation(x):
    m=mean(x)
    sum=0
    for i in range(len(x)):
        sum+=pow((x[i]-m),2)
    
    return math.sqrt(sum/(len(x)-1))

def selectionSort(x):
    for i in range(len(x)-1):
        xmin=x[i]
        xidx=i
        for j in range(i+1,len(x)):
            if xmin>x[j]:
                xmin=x[j]
                xidx=j
        if xidx!=i:
            x[xidx]=x[i]
            x[i]=xmin

def countNumbers(x):
    count=10*[0]
    for i in range(len(x)):
        a=x[i]
        count[a]+=1
    
    for i in range(len(count)):
        print(i,"숫자",count[i],"번 발생")
        
def main():
    s = input("0과 9사이의 정수값들을 입력하시오 : ") 
    item=s.split()
    numbers=[eval(x) for x in item]
    
    minIdx, minVal = indexOfSmallestElement(numbers)
    print("최소값 index :", minIdx,  "최소값 :", minVal)
    
    print("평균 : ", mean(numbers), "표준편차 : ", deviation(numbers))
    countNumbers(numbers)
    selectionSort(numbers)
    
    print(numbers)

main()



