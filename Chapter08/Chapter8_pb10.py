def decimalToBinary(value):
    h=""
    while value>0:
        b=value%2
        h=str(b)+h
        value//=2
    return h

def main():
    decimal=eval(input("십진수를 입력하세요: "))
    
    s=decimalToBinary(decimal)
    
    print("2진수: ", s)
    
main()
