def findminmax(a):
    fmax=max(a)
    fmin=min(a)
    return fmin,fmax

def findsum(a):
    sum=0
    for i in range(len(a)):
        sum+=a[i]
    return sum

def maplambda(a):
    a2=[0]*len(a)
    for i in range(len(a)):
        a2[i]=a[i]**2
    
    return a2

def filterlambda(a):
    af=[]
    for i in range(len(a)):
        if a[i]>0:
            af.append(a[i])
    
    return af


if __name__ == "__main__":
    a = [1, -2, 3, -5, 8, -3]
    print(findminmax(a))
    print(findsum(a))
    print(maplambda(a))
    print(filterlambda(a))