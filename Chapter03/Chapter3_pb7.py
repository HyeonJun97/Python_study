#Q3.7
import time

a=int(time.time()%65)
a=65+a%26   # A=65,Z=90
print(chr(a))