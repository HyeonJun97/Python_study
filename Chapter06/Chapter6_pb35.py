#Q6.35

import random

def getrandomcharacter(ch1, ch2):
    return chr(random.randint(ord(ch1),ord(ch2)))


def getrandomupperletter():
    return getrandomcharacter('A','Z')

def main():
    count=0
    for i in range (0, 10000):
        a=getrandomupperletter()
        if a=='A':
            count+=1
            
    print("A의 개수는",count,"입니다.")
    
main()
