#Q4.16
import random

computer=random.randint(0,2)
user=eval(input("가위(0), 바위(1), 보(2): "))

if computer==0 and user==0:
    print("컴퓨터는 가위 입니다. 당신은 가위 입니다. 비겼습니다.")
elif computer==0 and user==1:
    print("컴퓨터는 가위 입니다. 당신은 바위 입니다. 당신이 이겼습니다.")
elif computer==0 and user==2:
    print("컴퓨터는 가위 입니다. 당신은 보 입니다. 당신이 졌습니다.")
elif computer==1 and user==0:
    print("컴퓨터는 바위 입니다. 당신은 가위 입니다. 당신이 졌습니다.")
elif computer==1 and user==1:
    print("컴퓨터는 바위 입니다. 당신은 바위 입니다. 비겼습니다.")
elif computer==1 and user==2:
    print("컴퓨터는 바위 입니다. 당신은 보 입니다. 당신이 이겼습니다.")
elif computer==2 and user==0:
    print("컴퓨터는 보 입니다. 당신은 가위 입니다. 당신이 이겼습니다.")
elif computer==2 and user==1:
    print("컴퓨터는 보 입니다. 당신은 바위 입니다. 당신이 졌습니다.")
else:
    print("컴퓨터는 보 입니다. 당신은 보 입니다. 비겼습니다.")