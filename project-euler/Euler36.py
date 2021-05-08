#Author DownToSky
#Euler Problem 36

#Returns the binary representation of a number in String
#Methode for converting to binary:
#ToBinary(6):
#6=2*3+0
#3=2*1+1
#1=2*0+1
#Then put all of the remainders in a sequence from the last remainder to the first: 110
def ToBinary(number):
    quotient=number
    binary=""
    while quotient!=0:
        binary=str(int(quotient%2))+binary
        quotient=int(quotient/2)
    return binary

#Converts the input to string and checks if its a palindrome
def isPali(seq):
    pattern=str(seq)
    j=len(pattern)-1
    i=0
    while i<=j:
        if pattern[i]!=pattern[j]:
            return False
        i+=1
        j-=1
    return True

sum=0
for i in range(0,1000000):
    if isPali(i)==True and isPali(ToBinary(i))==True:
        sum+=i
        
print(sum)