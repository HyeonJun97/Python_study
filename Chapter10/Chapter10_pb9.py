
def main():
    s=input("숫자를 입력하세요: ")
    item=s.split()
    number=[eval(x) for x in item]
    
    m=mean(number)
    d=deviation(number)
    
    print("평균은", format(m,'.2f'), "입니다.")
    print("표준편차는", format(d,'.5f'), "입니다.")

def mean(x):
    sum=0
    for i in range(len(x)):
        sum+=x[i]
        
    return sum/len(x)

def deviation(x):
    m=mean(x)
    n=len(x)
    sum=0
    
    for i in range(len(x)):
        sum+=((x[i]-m)**2)
        
    return (sum/n)**0.5

main()
