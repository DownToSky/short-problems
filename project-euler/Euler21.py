#Author DownToSky
#Euler Problem 21

import math
#Calculates the d(n) which is sum of proper divisors of n
def d(n):
    sqrt=int(math.sqrt(n))
    sum=1
    for i in range(2,sqrt):
        if n%i==0:
            sum+=i
            sum+=n/i
    if sqrt*sqrt==n:
        sum+=sqrt
    return sum

#An interesting observation from amicable pair definition:
#m!=n, d(n)=m, d(m)=n
#so d(d(n))=d(m)=n where d(n)!=n
#so if n is an amicable number, d(d(n))=n

#The rest is a simple traversal (one is not amicable)
ans=0
for n in range(2,10000):
    if d(n)!=n and d(d(n))==n:
     ans+=n
print(ans)

#If the alternate definition wasn't found, it would be possible to make another function and do the traversal