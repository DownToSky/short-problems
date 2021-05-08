#Author DownToSky
#Euler Problem 26

#Trying several examples by hand will make this problem easy:
#The procedures to find 1/7:
#devide 1 by 7:     currentResult=0
#multiply last remainder by 10 and devide by 7: currentResult=0.1 (2nd step)
#multiply last remainder by 10 and devide by 7: currentResult=0.14
#multiply last remainder by 10 and devide by 7: currentResult=0.142
#multiply last remainder by 10 and devide by 7: currentResult=0.1428
#multiply last remainder by 10 and devide by 7: currentResult=0.14285
#multiply last remainder by 10 and devide by 7: currentResult=0.142857
#multiply last remainder by 10 and devide by 7: currentResult=0.1428571 (8th step)
#From the last step, the remainders are gonna be reapeted since the remainder in last step
#is equal to the remainder in step 2. From this we know that the 2nd step will be
#repeated until step 8 so the cycle is produce in steps 2,3,4,5,6,7

#Two sidenotes:
#1)If the remainder at any point is 0, the number has no recurring cycles since the 
#decimals terminate
#2)It is interesting to know that the length of cycle in number 1/d is bounded to a maximum
#of d-1. This is because of the fact that n/d has d-1 unique(non-zero) remainders(from 0,1,...,d-1)
#so after a maximum of d-1 divisions, the next remainder will be the same as one of the old ones 

#Accepts d as the input and returns the legth of the recurring cycle in 1/d
def LenOfCycle(divisor):
    dividend=1
    cycleLength=0
    dividends=[]
    while True:
        dividend*=10
        if dividend==0:
            break
        if dividend in dividends:
            #For 1/7 this will be [1,4,2,8,5,7] and 1 will be reapeted, so all numbers from 1,4,..,7 are in the cycle:
            cycleLength= len(dividends)-dividends.index(dividend) 
            break
        dividends.append(dividend)
        dividend=dividend%divisor
    return cycleLength

maxLen=0
maxNum=1
for i in range(1,1000):
    currentCycleLen= LenOfCycle(i)
    if maxLen<currentCycleLen:
        maxLen=currentCycleLen
        maxNum=i
print(str(maxNum))
        
        
    