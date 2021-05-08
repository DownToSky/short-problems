#Author DownToSky
#Euler Problem 1

#WE have to check each number for 3, or 5, or 3 and 5(15) divisions
#but anything that is not divided by 3 is also not divided by 5
#we we only need to check each number for mod 3 and if 3 doesnt divide
#then check for mod 5
sum = 0
for x in range(1,1000):
    if x%3==0:
        sum = sum+x
    else:
        if x%5==0:
            sum = sum+x
print (str(sum))