import random
import os.path
import sys

f1=input("파일 이름을 입력하세요: ").strip()

if os.path.isfile(f1):
    print("파일이 이미 존재합니다.")
    sys.exit()

outfile=open(f1,"w")

line=0

for i in range(100):
    outfile.write(str(random.randint(1,100)) + " ")
    line+=1
    if line==10:
        line=0
        outfile.write("\n")

outfile.close()

infile = open(f1, "r")

s = infile.read()
numbers = [eval(x) for x in s.split()]
numbers.sort()

for number in numbers:
    print(number, end = " ")
    line+=1
    if line==10:
        line=0
        print("\n")
    
infile.close()