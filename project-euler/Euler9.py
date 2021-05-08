#Author DownToSky
#Euler Problem 9
def arePythagTriplet(a,b,c):
    if a*a+b*b==c*c:
        return True
    else:
        return False

#A very useful observation is the following:
#If a+b+c=n and a<=b<=c  then a is at most a=b=c
#a+b+c=3a=n hence  a=n/3
#Maximizing this for b is when b=c and a=0
#a+c=n hence b=n/2       
for a in range(1,int(1001/3)):
    for b in range(a,int(1001/2)):
        c=1000-a-b
        if arePythagTriplet(a,b,c):
            print(str(a*b*c))