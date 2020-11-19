def main():
    while True:
        try:
            filename=input("파일이름을 입력하세요: ").strip()
            infile=open(filename,"r")
            break
        except IOError:
            print(filename,"는 존재하지 않습니다.")
    
    charcount=0
    wordcount=0
    linecount=0
    
    for line in infile:
        charcount+=len(line)
        linecount+=1
        
        word=line.split()
        wordcount+=len(word)
        
    print("문자",str(charcount))
    print("단어",str(wordcount))
    print("행", str(linecount))
    
    infile.close()

main()
