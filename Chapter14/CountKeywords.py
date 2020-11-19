import os.path
import sys

def main():
    keyWords = {"and", "as", "assert", "break", "class",
                "continue", "def", "del", "elif", "else",
                "except", "False", "finally", "for", "from",
                "global", "if", "import", "in", "is", "lambda",
                "None", "nonlocal", "not", "or", "pass", "raise",
                "return", "True", "try", "while", "with", "yield"}

    filename = input("파이썬 소스 코드 파일명을 입력하세요: ").strip()

    if not os.path.isfile(filename):  # 파일이 존재하는지 검사한다.
        print("파일", filename, "이 존재하지 않습니다.")
        sys.exit()

    infile = open(filename, "r") # 파일은 오픈한다.

    text = infile.read().split() # 파일을 읽고 단어 단위로 분리한다.

    count = 0
    for word in text:
        if word in keyWords:
            count += 1

    print(filename, "에", count, "개의 키워드가 포함되어 있습니다.")

main()
