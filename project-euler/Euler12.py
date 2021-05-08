#Author DownToSky
#Euler Problem 12
import math
"""
    We know if n=AB (A,B both int) then, either A>sqrt(n) or B>sqrt(n).
    Proof:
    Suppose that it is wrong, meaning that both A,B<sqrt(n), then ab!=n which cannot
    be right since we assumed n=Ab. From this we can assume that whenever we find a 
    number like 1<=A<sqrt(n) that is a divisor of n, we can also find a number like B in a way
    tha sqrt(n)<B<=n, hence whenever we find a divisor of n in the range (1,sqrt(n)) we know we 
    have actually found two divisors. The only special case is when sqrt(n) is an integer, in which
    we know sqrt(n) is also a divisor of n(since sqrt(n)^2==n)
    Not using this fact will result in a very long computation time.
"""
def numOfDivisors(n):
    count =0
    sqrt=int(math.sqrt(n))
    for i in range (1,sqrt):
        if n%i==0:
            count +=2
    if sqrt*sqrt==n:
        count+=1
    return count
"""
we can recursively define triangle numbers by:
T[1]=1
T[i]=i+T[i-1]
T[1]=1, T[2]=2+t[1]=3,  T[3]=3+T[2]=6, and so on ...
________________
Another possibly better approach is this definition:
T[i]=1+2+3+....+i = i(i-1)/2
"""

i=1
triagNum=0
while True:
    triagNum+=i
    if numOfDivisors(triagNum)>500:
        print (str(triagNum))
        break
    i+=1
