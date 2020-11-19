#Q4.7
a, b, c=eval(input("세 정수를 입력하세요: "))

if a<b and a<c and b<c:
    print(a, b, c)
elif a<b and a<c and b>c:
    print(a, c, b)
elif a<b and a>c:
    print(c, a, b)
elif a>b and a>c and b>c:
    print(c, b, a)
elif a>b and a>c and b<c:
    print(b, c, a)
else:
    print(b, a, c)