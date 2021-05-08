#Author DownToSky
#Euler Problem 25

#Can't use the recursive function in Problem 2
#since the running time is of exponential order
#We can change it to linear order if we start with
#two first element and find the next one by adding
#the last two
Fn_2= 1
Fn_1=1
index=2
while True:
    index+=1
    
    currentFib=Fn_1+Fn_2
    if len(str(currentFib))==1000:
        print(str(index))
        break
    Fn_2=Fn_1    
    Fn_1=currentFib
