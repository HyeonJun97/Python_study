import time

class StopWatch:
    def __init__(self):
        self.__startTime=time.time()
    
    def start(self):
        self.__startTime=time.time()
    
    def stop(self):
        self.__endTime=time.time()
        
    def getElapsedTime(self):
        return int((self.__endTime-self.__startTime)*1000)
        
def main():
    SW=StopWatch()
    sum=0
    
    for i in range(1,1000001):
        sum+=i
    
    SW.stop()
    
    print("Time:",SW.getElapsedTime(),"ms")

main()
