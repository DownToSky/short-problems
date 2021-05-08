#Author DownToSky
#Euler Problem 27
import math

def isPrime(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    sqrt=int(math.sqrt(n))
    for i in range(3,sqrt+1,2):
        if n%i==0:
            return False
    return True
  
def NumberOfConsequtive(a,b):
    numOfConsPrimes=0
    n=0
    while True:
        if isPrime(n*n+a*n+b):
            numOfConsPrimes+=1
            n+=1
        else:
            break
    return numOfConsPrimes

max_A_B=[0,0]   #Contains the A and B with the maximum number of consequitive primes
maxConsPrimesFound=0 #Max number of primes found for an A and B
for i in range(-999,1000):
    for j in range(-999,1000):
        temp=NumberOfConsequtive(i,j)
        if temp>maxConsPrimesFound:
            maxConsPrimesFound=temp
            max_A_B=[i,j]
            
print(str(max_A_B[0]*max_A_B[1]))