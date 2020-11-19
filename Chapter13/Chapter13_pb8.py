
filename=input("암호화할 파일 이름을 입력하세요: ").strip()
outfilename=input("암호화될 파일의 이름을 입력하세요: ").strip()

infile=open(filename,"r")
s=infile.read()
infile.close()

encoder=''

for i in range(len(s)):
    encoder+=chr(ord(s[i]) +5)


outfile=open(outfilename,'w')
outfile.write(encoder)
outfile.close()

