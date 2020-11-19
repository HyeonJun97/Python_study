
s=input("숫자를 입력하세요: ").strip()
item=s.split()
number=[eval(x) for x in item]

dic={}

for i in number:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

maxc=max(dic.value())

pairs=list(dic.item())
items=[[x,y] for (x,y) in pairs]


for (x,y) in items:
    if y == maxc:
        print(x, end=' ')
        
main()
