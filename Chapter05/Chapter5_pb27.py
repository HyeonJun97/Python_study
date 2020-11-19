#Q5.27

sum=0
i=1
count=1

while i<1000000:
    if i%2==1:
        number=1/count
    else:
        number=(-1)/count
    
    i+=1
    count+=2
    
    sum+=number

sum*=4

print("pi=",format(sum,'.10f'))