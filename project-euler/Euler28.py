#Author DownToSky
#Euler Problem 28

#each nxn square is composed of 1x1,3x3,5x5,....,nxn sub squares. In other words:
#an n by n square is made of (2k-1)x(2k-1) for all integer ks such that 1=< k =<(n+1)/2
#We can call k the layer number
#For example, in the follwong square with width of 5:

#21 22 23 24 25
#20  7  8  9 10
#19  6  1  2 11
#18  5  4  3 12
#17 16 15 14 13

#The sum squares consist of:

#        (k=3)                     (k=2)              (k=1)
#   21 22 23 24 25         
#   20          10                7  8  9 
#   19          11      and       6     2      and     1
#   18          12                5  4  3 
#   17 16 15 14 13

#Also it is possible to show each square as a list of numbers:
#k=1:   1                                                   (1 number)
#k=2:   2,3,4,5,6,7,8,9                                     (8 numbers)
#k=3:   10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25     (16 numbers)

#The follwing is true for all layers except when k=1 (first layer):

#1)The count of numbers in each layer can be found by 4n-4 where n=2k-1(remeber that n was the width of the squares)
#This is found by counting the width 4 times and substracting the edges(since they've been counted twice each)

#2)The last number in a layer such as k is a part of the diagonal entries and its value is equal to n^2
#From this, and the fact that we have the width, we can guess that the third entry in the layer k is n^n-n or close to that, but
#since we logically substracted the edge(the third entry is at the edge of the square) twice we need to add 1 to it so the formula becomes:
#n^2-n+10
#With the same appraoch we see that:

#3)The third number on layer k that is a part of the diagonal entries is found by n^2-n+1 where n=2k-1          (+1 since 1 edge was substracted twice)
#4)The second number on layer k that is a part of the diagonal entries is found by n^2-2n+2 where n=2k-1        (+2 since 2 edges were substracted twice)
#5)The first number on layer k that is a part of the diagonal entries is found by n^2-3n+3 where n=2k-1         (+3 since 3 edges were substracted twice)

#The problem becomes a matter of iteratin through all layers until the width is equal to 1001 and add all
#four diagonal elemnts of that layer to the total sum


N=1001
sum=0
sum+=1      #Since the formula does not work for when n=1
for n in range(3,N+1,2):
    firstNumberInLayer=n*n
    secondNumberInLayer=n*n-n+1
    thirdNumberInLayer=n*n-2*n+2
    forthNumberInLayer=n*n-3*n+3
    sum+=firstNumberInLayer+secondNumberInLayer+thirdNumberInLayer+forthNumberInLayer
    
print(sum)
