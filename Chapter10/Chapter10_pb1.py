
def main():
    s=input("점수를 입력하세요: ")
    items=s.split()
    score=[eval(x) for x in items]

    mscore=max(score)

    for i in range (len(score)):
        if score[i] > mscore-10:
            print("학생",i,"의 점수는",score[i],"이고 성적은 A 입니다.")
        elif score[i]>mscore-20:
            print("학생",i,"의 점수는",score[i],"이고 성적은 B 입니다.")
        elif score[i]>mscore-30:
            print("학생",i,"의 점수는",score[i],"이고 성적은 C 입니다.")
        elif score[i]>mscore-40:
            print("학생",i,"의 점수는",score[i],"이고 성적은 D 입니다.")
        else:
            print("학생",i,"의 점수는",score[i],"이고 성적은 F 입니다.")

main()
