#By DownToSky
#Euler Problem 5
def divisbleByAll(n):
    for x in range(2, 21):
        if n%x!=0:
            return False
    return True
#Brute Force:
#If we find the biggest shared roorts of all number until 20 we can find it MUCH FASTER!
#for example for 1-10: 8*9*5*7
#and for 20 is: 16*9*5*7*11*13*17*19 (wich is also the answer to this euler problem)

number = 1
while number>0:
    if divisbleByAll(number):
        print ("answer: "+ str(number))
        break
    else:
        number = number+1
