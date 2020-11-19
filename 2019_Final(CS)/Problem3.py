from P3 import findminmax
from P3 import findsum
from P3 import maplambda
from P3 import filterlambda

def main():
    a = [1, -2, 3, -5, 8, -3]
    mina,maxa=findminmax(a)
    print("a 리스트의 최소, 최대값은 ", mina, maxa)
    suma=findsum(a)
    print("a 리스트 합은 ", suma)
    x=maplambda(a)
    print("a 리스트의 제곱은 ", x)
    y=filterlambda(a)
    print("a 리스트에서 음수를 제거하면 ", y)
    
main()