#Author DownToSky
#Euler Problem 3
import math

#We can use the fact that every prime factor of a number such as n is 
#always between 1 and sqrt(n) to improve the computation time
def isPrime(n):
    #2 is the only even prime number:
    if (n%2==0 and n!=2) or n<1:
        return False
    else:
        counter =0
        i=1
        while i*i<=n:
            if n%i==0:
                counter = counter+1
            i=i+2
        #since i starts from 1 all prime and stops at sqrt(n)
        #all the prime numbers given to function will have counter=1
        if counter>1:
            return False
        else:
            return True

#Again, we only need to check until sqrt(600851475143) and not to 600851475143            
largestPrime=1
number = 600851475143
for x in range(2,int(math.sqrt( number))):
    if isPrime(x) and number%x==0:
        largestPrime=x
    
print ("final largest prime is: "+str(largestPrime))
