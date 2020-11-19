def binaryToHex(binaryValue):
    h=""
    while binaryValue>0:
        a=binaryValue%10000
        b=0
        for i in range(4):
            b+=((a%10)*(2**i))
            a//=10
        if b>=0 and b<=9:
            h=str(b)+h
        else:
            h=chr(ord('A')+b-10)+h
        
        binaryValue//=10000
    return h

def main():
    binary=eval(input("이진수를 입력하세요: "))
    
    s=binaryToHex(binary)
    
    print("16진수: ", s)
    
main()
