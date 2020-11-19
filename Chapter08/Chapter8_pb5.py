def count(s1,s2):
    scount=s1.count(s2)
    return scount
    
def main():
    s1=input("첫 번째 문자열을 입력하세요:").strip()
    s2=input("두 번째 문자열을 입력하세요:").strip()
    
    scount=count(s1,s2)
    
    print("빈도:",scount)
        
main()