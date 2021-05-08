#Author DownToSky
#Euler Problem 17

#Authors sidenote: Its possible to reduce the if-blocks for 100s and 1000s by
#adding the word in that digit("one", "two", etc.) to "hundred" or"thousand"
#but since we dont need to evaluate for numbers above 1000, I used the boring if blocks to make the function

#returns the number of characters in the word form of number n (including "and"), where 0<n<10000
def WordsInNumber(n):
    if n<1 or n>9999:
        return -1
        
    ans=0
    nextDigHasAND=False
    number=str(n)
    while len(number)<4:
        number ="0"+number
        
    if number[0]!="0":
        if number[0]=="1":#"oneThousand"
            ans+=11
            nextDigHasAND=True
        if number[0]=="2":#"twoThousand"
            ans+=11
            nextDigHasAND=True
        if number[0]=="3":#"threeThousand"
            ans+=13
            nextDigHasAND=True
        if number[0]=="4":#"fourThousand"
            ans+=12
            nextDigHasAND=True
        if number[0]=="5":#"fiveThousand"
            ans+=12
            nextDigHasAND=True
        if number[0]=="6":#"sixThousand"
            ans+=11
            nextDigHasAND=True
        if number[0]=="7":#"sevenThousand"
            ans+=13
            nextDigHasAND=True
        if number[0]=="8":#"eightThousand"
            ans+=13
            nextDigHasAND=True
        if number[0]=="9":#"nineThousand"
            ans+=12
            nextDigHasAND=True            
    if number[1]!="0":
        if nextDigHasAND==True:
            ans+=3
            nextDigHasAND=False
        if number[1]=="1":#"oneHundred"
            ans+=10
            nextDigHasAND=True
        if number[1]=="2":#"twoHundred"
            ans+=10
            nextDigHasAND=True
        if number[1]=="3":#"threeHundred"
            ans+=12
            nextDigHasAND=True
        if number[1]=="4":#"fourHundred"
            ans+=11
            nextDigHasAND=True
        if number[1]=="5":#"fiveHundred"
            ans+=11
            nextDigHasAND=True
        if number[1]=="6":#"sixHundred"
            ans+=10
            nextDigHasAND=True
        if number[1]=="7":#"sevenHundred"
            ans+=12
            nextDigHasAND=True
        if number[1]=="8":#"eightHundred"
            ans+=12
            nextDigHasAND=True
        if number[1]=="9":#"nineHundred"
            ans+=11
            nextDigHasAND=True
    if number[2]!="0":
        if nextDigHasAND==True:
            ans+=3
            nextDigHasAND=False
            
        if number[2]=="1":
            if number[3]=="0":#ten
                ans+=3
            if number[3]=="1":#eleven
                ans+=6
            if number[3]=="2":#twelve
                ans+=6
            if number[3]=="3":#Thirteen
                ans+=8
            if number[3]=="4":#Fourteen
                ans+=8
            if number[3]=="5":#fifteen
                ans+=7
            if number[3]=="6":#sixteen
                ans+=7
            if number[3]=="7":#seventeen
                ans+=9
            if number[3]=="8":#eighteen
                ans+=8
            if number[3]=="9":#nineteen
                ans+=8
        
            return ans #because for numbers between 9 and 20, both degits are only one word
                       #so there is no more counting left
        else:
            if nextDigHasAND==True:
                ans+=3
                nextDigHasAND=False
            if number[2]=="2":#"twenty"
                ans+=6
            if number[2]=="3":#"thirty"
                ans+=6
            if number[2]=="4":#"forty"
                ans+=5
            if number[2]=="5":#"fifty"
                ans+=5
            if number[2]=="6":#"sixty"
                ans+=5
            if number[2]=="7":#"seventy"
                ans+=7
            if number[2]=="8":#"eighty"
                ans+=6
            if number[2]=="9":#"ninety"
                ans+=6
    if number[3]!="0":
        if nextDigHasAND==True:
            ans+=3
            nextDigHasAND=False
        if number[3]=="1":#"one"
            ans+=3
        if number[3]=="2":#"two"
            ans+=3
        if number[3]=="3":#"three"
            ans+=5
        if number[3]=="4":#"four"
            ans+=4
        if number[3]=="5":#"five"
            ans+=4
        if number[3]=="6":#"six"
            ans+=3
        if number[3]=="7":#"seven"
            ans+=5
        if number[3]=="8":#"eight"
            ans+=5
        if number[3]=="9":#"nine"
            ans+=4
    return ans

ans=0
for i in range(1,1000+1):
    ans+=WordsInNumber(i)
print(ans)
