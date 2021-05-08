#Author DownToSky
#Euler Problem 10


import math
def isPrime(n):
    if (n%2==0 and n!=2) or n<1:
        return False
    else:
        counter =0
        i=1
        while i*i<=n:
            if n%i==0:
                counter = counter+1
            i=i+2
        if counter>1:
            return False
        else:
            return True
#Iterating through all numbers below 2000000
#we could count 2 as a prime and skip even numbers to improve this code            
sumOfPrimes=0
for i in range(2,2000000):
    if isPrime(i):
        sumOfPrimes+=i
print ("sum of all primes below 2,000,000 is: "+str(sumOfPrimes))