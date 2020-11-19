class MyPhone:
    def __init__(self, name, number):
        self.name=name
        self.number=number
        self.friends={}
    
    def printMyPhone(self):
        print("핸드폰 주인 :", self.name, end=', ')
        print("전화번호:", self.number)
        
    def addFriend(self, name, number):
        self.friends[name]=number
    
    def findFriend(self, name):
        chk=False
        for i in self.friends:
            if name in i:
                print(name,"의 전화번호는",self.friends[i],"입니다.")
                chk=True
        if chk==False:
            print(name,"이름이 전화번호부에 없습니다")
    
    def printFriends(self):
        print("친구 이름과 전화번호")
        for i in self.friends:
            print(i+str(" "+self.friends[i]))
        print("")
        

def main():
    p = MyPhone("홍길동", "0101112222")
    p.printMyPhone()
    p.addFriend("Lisa", "0103334444")
    p.addFriend("Monster", "0105556666")
    p.addFriend("정철", "0107778888")
    p.printFriends()
    p.findFriend("Lisa")
    p.findFriend("Elsa")
    
main()