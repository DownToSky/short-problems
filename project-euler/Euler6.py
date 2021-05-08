#Author DownToSky
#Euler Problem 6

#Note that 1+2+...+n=n(n-1)/2
#Using the fact that 1^2+2^2+...+n^2=n(n+1)(2n+1)/6 to
#improve this solution
firstSum =0
secondSum =0
for x in range(1, 101):
    firstSum=firstSum+ x*x
    secondSum=secondSum+ x
secondSum=secondSum*secondSum
print (str(secondSum-firstSum))