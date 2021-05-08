#Author DownToSky
#Euler Problem 4

#Checks to see in n is palindromic by converting n to 
#string and checking if the string is a palindrome
def isPalindromic(n):
    stringN = str(n)
    leftBound = 0
    rightBound = len(stringN)-1
    isPali = True
    while leftBound<rightBound:
        if stringN[leftBound]!=stringN[rightBound]:
            isPali=False
            break
        rightBound=rightBound-1
        leftBound=leftBound+1
    return isPali

#Iterate all 3 digit numbers and see if their multiple is
#palindromic. Starting from the largest 3 digits guarentees 
#that the first such numbers found are also the answer
i=999
isFound = False
largestPali=0
while i>99:
    j=999
    while j>99:
        if isPalindromic(i*j) and i*j > largestPali:
            largestPali=i*j
        j=j-1
    i=i-1

print("answer: "+str(largestPali))
