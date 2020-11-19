def checkstring(s1,s2):
    
    check=s2.find(s1)
    
    if check==-1:
        return False
    else:
        return True

def main():
    s1=input("첫 번째 문자열을 입력하세요:").strip()
    s2=input("두 번째 문자열을 입력하세요:").strip()
    
    check=checkstring(s1,s2)
    
    if check==True:
        print("부분문자열")
    else:
        print("부분문자열아님")
        
main()