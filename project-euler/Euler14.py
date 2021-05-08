#Author DownToSky
#Euler Problem 14

#returns the legth of the collatz sequence starting with number n
def sequenceLength(n):
    count =0
    while n!=1:
        if n%2==0:
            n=n/2
            count+=1
        else:
            n=3*n+1
            count+=1
    #since we never count the last number that blongs to the sequence: 1
    count+=1
    return count
#Iterating through all numbers and finding the one with largest seq length    
largestSq=0
largestStart=1
for i in range(1,1000000+1):
    currentSqLength=sequenceLength(i)
    if(largestSq<currentSqLength):
        largestStart=i
        largestSq=currentSqLength
print(largestStart)