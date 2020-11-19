
filename=input("복호화할 파일 이름을 입력하세요: ").strip()
filename2=input("복호화될 파일 이름을 입력하세요: ").strip()

infile=open(filename,'rt')

s=infile.read()
infile.close()


decoder=''

for i in range(len(s)):
    decoder+=chr(ord(s[i]) - 5)

outfile=open(filename2,'wt')
outfile.write(decoder)
outfile.close()
