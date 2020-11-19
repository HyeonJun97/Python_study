number = eval(input("양의 정수를 입력하시오 : "))

while number != 0:
    
   n=number%10
   temp=n
   bi=""
   number//=10
   
   if n==0:
       bi=str(0)
       
   while temp !=0:
       a=(temp%2)
       temp//=2
       bi=str(a)+bi

   if n%2==0:
        print(n,"짝수",bi)
   else:
        print(n,"홀수",bi)