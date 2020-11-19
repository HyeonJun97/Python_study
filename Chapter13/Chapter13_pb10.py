class Rational:
    def __init__(self, numerator = 0, denominator = 1):
        divisor = gcd(numerator, denominator)
        self.__numerator = (1 if denominator > 0 else -1) \
            * int(numerator / divisor)
        self.__denominator = int(abs(denominator) / divisor)
        
        if denominator==0:
            raise RuntimeError('Zero in denominator')

    # 자신의 유리수에 지정된 유리수를 더한다.
    def __add__(self, secondRational):
        n = self.__numerator * secondRational[1] + \
            self.__denominator * secondRational[0]
        d = self.__denominator * secondRational[1]
        return Rational(n, d)

    # 자신의 유리수에서 지정된 유리수를 뺀다.
    def __sub__(self, secondRational):
        n = self.__numerator * secondRational[1] - \
            self.__denominator * secondRational[0]
        d = self.__denominator * secondRational[1]
        return Rational(n, d)

    # 자신의 유리수와 지정된 유리수를 곱한다.
    def __mul__(self, secondRational):
        n = self.__numerator * secondRational[0]
        d = self.__denominator * secondRational[1]
        return Rational(n, d)

    # 자신의 유리수를 지정된 유리수로 나눈다.
    def __truediv__(self, secondRational):
        n = self.__numerator * secondRational[1]
        d = self.__denominator * secondRational[0]
        return Rational(n, d)

    # 자신의 유리수를 실수 값으로 반환한다.
    def __float__(self):
        return self.__numerator / self.__denominator

    # 자신의 유리수를 정수 값으로 반환한다.
    def __int__(self):
        return int(self.__float__())

    # 문자열 표현을 반환한다.
    def __str__(self):
        if self.__denominator == 1:
            return str(self.__numerator)
        else:
            return str(self.__numerator) + "/" + str(self.__denominator)

    def __lt__(self, secondRational):
        return self.__cmp__(secondRational) < 0

    def __le__(self, secondRational):
        return self.__cmp__(secondRational) <= 0

    def __gt__(self, secondRational):
        return self.__cmp__(secondRational) > 0

    def __ge__(self, secondRational):
        return self.__cmp__(secondRational) >= 0

    # 두 숫자를 비교한다.
    def __cmp__(self, secondRational):
        temp = self.__sub__(secondRational)
        if temp[0] > 0:
            return 1
        elif temp[0] < 0:
            return -1
        else:
            return 0

    # 인덱스 연산자를 사용하여 분자와 분모를 반환한다.
    def __getitem__(self, index):
        if index == 0:
            return self.__numerator
        else:
            return self.__denominator

def gcd(n, d):
    n1 = abs(n);
    n2 = abs(d)
    gcd = 1

    k = 1
    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k == 0:
            gcd = k
        k += 1

    return gcd

def main():
    r1=Rational(1,2)
    r2=Rational(2,0)
    
main()
