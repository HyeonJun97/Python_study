from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

# 여기에 tkinter filedilog 모듈을 이용하기 위한 코드 작성

def phoneBook_read(phoneBook):
    # 여기에 전화번호부를 읽기 위한 코드 작성
    filename=askopenfilename()
    count=0
    while True:
        try:
            infile=open(filename,"rt")
            break
        except IOError:
            print("파일",filename,"이/가 존재하지 않습니다.")
    
    for i in infile:
        count+=1
        item=i.split()
        phone=[x for x in item]
        phoneBook[phone[0]]=phone[1]
    print("총 ", count, " 명의 전화번호부가 upload되었습니다.")
    infile.close()
    
def phoneBook_search(phoneBook):
    # 여기에 전화번호를 검색하기 위한 코드 작성
    s=input("검색할 이름을 입력하시오. : ")
    chk=False
    for i in phoneBook.keys():
        if s in i:
            print("해당 이름이 검색되었습니다.")
            print("이름/번호 :",i,phoneBook[i])
            chk=True
    if chk==False:
        print("해당 이름이 검색되지 않았습니다.")
    
def phoneBook_insert(phoneBook):
    # 여기에 전화번호를 추가하기 위한 코드 작성    
    s=input("추가할 이름과 번호를 입력하시오. : ")
    item=s.split()
    phone=[x for x in item]
    phoneBook[phone[0]]=phone[1]
    print(s,"전화번호가 추가되었습니다.")
    
def phoneBook_save(phoneBook):
    # 여기에 전화번호부를 저장하기 위한 코드 작성
    filename=asksaveasfilename()
    outfile=open(filename,'wt')
    for i in phoneBook.keys():
        a=(str(i)+str(" ")+str(phoneBook[i])+"\n")
        #a=f'{i} {phoneBook[i]}\n'
        outfile.write(a)
    outfile.close()
    print(filename,"파일에 전화번호가 저장되었습니다.")


def main():

    print("전화번호부 파일을 선택하시오 !")
    phoneBook = {}
    phoneBook_read(phoneBook)
    
    while True:
        print("\n전화번호부 기능 : ")
        print("검색(1), 추가(2), 저장(3), 종료(0)")
        sel = eval(input("원하는 메뉴의 번호를 선택하시오. : "))
        if sel == 1:
            phoneBook_search(phoneBook)
        elif sel == 2:
            phoneBook_insert(phoneBook)
        elif sel == 3:
            phoneBook_save(phoneBook)
        elif sel == 0:
            break
        else:
            print("번호가 잘못입력되었습니다. 다시 입력하시오. ")

main() # main 함수를 호출한다.