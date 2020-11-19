
isbn=input("ISBN-10의 첫 9자리 문자열을 입력하세요:")

checksum=0

for i in range(len(isbn)):
    checksum+=(int(isbn[i])*(i+1))

checksum%=11

if checksum==10:
    print(isbn+"X")
else:
    print(isbn+str(checksum))
    