#Author DownToSky
#Euler Problem 20

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
sum =0
fact=str(fact(100))
for i in range(0,len(fact)):
    sum+=int(fact[i])
print(sum)