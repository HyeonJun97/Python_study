#Q6.5

def displaySortedNumbers(num1, num2, num3):
    
    if num1<num2 and num1<num3 and num2<num3:
        print(num1,num2,num3, end='')
    elif num1<num2 and num1<num3 and num2>num3:
        print(num1,num3,num2, end='')
    elif num1<num2 and num1>num3:
        print(num3,num1,num2, end='')
    elif num1>num2 and num2<num3 and num1>num3:
        print(num2,num3,num1, end='')
    elif num1>num2 and num2<num3 and num1<num3:
        print(num2,num1,num3, end='')
    else:
        print(num3,num2,num1, end='')

def main():
    n1,n2,n3=eval(input("세 수를 입력하세요: "))
    
    print("정렬된 숫자는", end=' ')
    displaySortedNumbers(n1,n2,n3)
    print(" 입니다.")

main()
