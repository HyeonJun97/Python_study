#Q5.22

count = 0 
number = 2
linecount=8

print("2~1000 사이의 소수 출력")

while number<=1000:
    isPrime = True
    divisor = 2
    
    while divisor <= number / 2:
        if number % divisor == 0:
            isPrime = False
            break
        divisor += 1

    if isPrime:
        count += 1
        print(format(number, '5d'), end = '')
        
        if count % linecount == 0:
            print()

    number += 1
