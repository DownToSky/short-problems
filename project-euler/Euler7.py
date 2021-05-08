#Author DownToSky
#Euler Problem 7

#Using the knowledge that half of the factors of n are between
#n and sqrt(n) to reduce the computation time greatly
numberOfPrimes=0
i=2             #Starting from 2 since we know 1 is not prime
while i>0:
    j=1
    numberOfDivisbles=0
    while j*j<=i:
        if i%j==0:
           numberOfDivisbles +=1
        j=j+1
    if numberOfDivisbles==1:
        numberOfPrimes+=1
    if numberOfPrimes==10001:
        print(str(i))   #Print 10,001st prime
        break
    #two is the only even prime number
    if i>2:
        i=i+2
    else:
        i=i+1