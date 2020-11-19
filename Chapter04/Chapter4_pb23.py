#Q4.23

import random

a=random.randint(1,13)
b=random.randint(1,4)

if b==1:
    if a>=2 and a<=10:
        print("당신이 뽑은 카드는 크로바",a,"입니다.")
    elif a==1:
        print("당신이 뽑은 카드는 크로바 A입니다.")
    elif a==11:
        print("당신이 뽑은 카드는 크로바 J입니다.")
    elif a==12:
        print("당신이 뽑은 카드는 크로바 Q입니다.")
    elif a==13:
        print("당신이 뽑은 카드는 크로바 K입니다.")
        
elif b==2:
    if a>=2 and a<=10:
        print("당신이 뽑은 카드는 다이아몬드",a,"입니다.")
    elif a==1:
        print("당신이 뽑은 카드는 다이아몬드 A입니다.")
    elif a==11:
        print("당신이 뽑은 카드는 다이아몬드 J입니다.")
    elif a==12:
        print("당신이 뽑은 카드는 다이아몬드 Q입니다.")
    elif a==13:
        print("당신이 뽑은 카드는 다이아몬드 K입니다.")
        
elif b==3:
    if a>=2 and a<=10:
        print("당신이 뽑은 카드는 하트",a,"입니다.")
    elif a==1:
        print("당신이 뽑은 카드는 하트 A입니다.")
    elif a==11:
        print("당신이 뽑은 카드는 하트 J입니다.")
    elif a==12:
        print("당신이 뽑은 카드는 하트 Q입니다.")
    elif a==13:
        print("당신이 뽑은 카드는 하트 K입니다.")
        
elif b==4:
    if a>=2 and a<=10:
        print("당신이 뽑은 카드는 스페이드",a,"입니다.")
    elif a==1:
        print("당신이 뽑은 카드는 스페이드 A입니다.")
    elif a==11:
        print("당신이 뽑은 카드는 스페이드 J입니다.")
    elif a==12:
        print("당신이 뽑은 카드는 스페이드 Q입니다.")
    elif a==13:
        print("당신이 뽑은 카드는 스페이드 K입니다.")