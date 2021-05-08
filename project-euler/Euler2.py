from utils import fib
#Author DownToSky
#Euler Problem 2

ans=0
n=0
f=fib._Fib1(n)
while f<=4000000:
	if f%2==0:
		ans+=f
	n+=1
	f=fib._Fib1(n)
print(ans)
