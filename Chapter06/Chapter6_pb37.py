#Q6.37

import turtle
import random

def getrandomcharacter(ch1, ch2):
    return chr(random.randint(ord(ch1),ord(ch2)))

def getrandomlowletter():
    return getrandomcharacter('a','z')

def main():
    turtle.penup()
    for i in range (0, 7):
        for j in range (0, 15):
            turtle.goto(0+20*j,0-20*i)
            turtle.write(getrandomlowletter())
    
    turtle.done()

main()
