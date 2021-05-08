#Author DownToSky
#Euler Problem 23

import math

#Returns true if the inpute is abundant number
def isAbundant(n):
    if n<12:    #12 is known as the smallest abundant number
        return False
    divSum=1    #one properly dvivides all positive numbers
    sqrt=int(math.sqrt(n))
    for i in range(2,sqrt):
        if n%i==0:
            divSum+=i+n/i
    if n%sqrt==0:
        if sqrt*sqrt==n:
            divSum+=sqrt
        else:
            divSum+=sqrt+n/sqrt
    if divSum>n:
        return True
    else:
        return False
    
#Finding all abundants below 28123 
abundants=[] 
for i in range(1,28123):
    if isAbundant(i):
        abundants.append(i)
#Finding which numbers are abundants
sumOfAbundants=[False]*28123    #For each number below the limit we define a False if the number is not sum of two abundants and True if it is
for i in range(0,len(abundants)):
    for j in range(0,len(abundants)):
        if abundants[i]+abundants[j]<28123:
            sumOfAbundants[abundants[i]+abundants[j]]=True
ans=0
for i in range(0,28123):
    if sumOfAbundants[i]==False:
        ans+=i
print(ans)