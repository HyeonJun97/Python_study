import time

currenttime=time.time()

tsecond=int(currenttime)

csecond=tsecond%60
tminute=tsecond//60

cminute=tminute%60
thour=tminute//60

chour=thour%24

print("현재시간은", chour,":", cminute, ":",csecond, "입니다.")