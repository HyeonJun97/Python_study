#Q4.22
x, y=eval(input("점의 좌표값을 입력하세요: "))

if (x<5 and x>-5) and (y<2.5 and y>-2.5):
    print("점 (",x,",",y,")은 사각형 내부에 있습니다.")
else:
    print("점 (",x,",",y,")은 사각형 내부에 있지 않습니다.")    