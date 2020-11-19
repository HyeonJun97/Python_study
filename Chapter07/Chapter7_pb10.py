import time

class Time:
    def __init__(self):
        self.__second=(int(time.time())%60)
        self.__minute=(int(time.time())//60%60)
        self.__hour=(int(time.time())//60//60%24)
    
    def getsecond(self):
        return self.__second
    def getminute(self):
        return self.__minute
    def gethour(self):
        return self.__hour
    
    def setTime(self, elapseTime):
        self.__second=elapseTime%60
        self.__minute=elapseTime//60%60
        self.__hour=elapseTime//60//60%24
    
def main():
    t=Time()
    
    print("현재 시간은",t.gethour(),":",t.getminute(),":",t.getsecond())
    
    a=eval(input("소요 시간을 입력하세요: "))
    
    t.setTime(a)
    
    print("소요 시간의 시:분:초는", t.gethour(),":",t.getminute(),":",t.getsecond())
    

main()
