#Author DownToSky
#Euler Problem 18

#This problem uses a similar approach to lattice paths in problem 15
#Starting from the lowest positions we find the maximum to that position and 
#build it up till we get to the top.

#Imagine the followong triangle:

#       a00
#   a10     a11
#a20    a21     a22
#where a[i][j] is the parent of a[i+1][j] and a[i+1][j+1].
# For example, if a00=10, a10=8 , a11=9, a20=6, a21=9, a22=3,we would have have:
#       10
#   8       9
#6      9       3

#We can recursively find the sum of maximum path from position a[i][j] to the lowest level by this recursive definition:
#Basis:The maximum paths for each position in the lowest level are equal to the number in that position
#Recursive step: The sum of maximum path numbers from position a[i][j] to bottom is the result of the sum of
#the value at position a[i][j] plus the greatest value of the sum of maximum path in it's childrens positions

#To find sum of maximum path in the mentioned example:
#Basis:(finds the sum of maximum path for lowest level)
#       a00
#   a10     a11
#6       9       3
#Recursive step for on layer above:(finds the sum of maximum path for each position on the previous level)
#               a00
#   8+max(6,9)     9+max(9,3)
#6              9               3
#Recursive step for highest level:(finds the sum of maximum path for each position on the previous level)
#    10+max(18,17)
#   17     18
#6      9      3
#Which will result in:
#       28
#   17     18
#6      9      3
#28 would be the answer

#Whats great about this approach is that not only it needs to calculate the sum of path for each position
#only once - as opposed to traversing all paths, but also will evaluate the the sum of maximum path for every position!
list=[
[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20,  4 ,82, 47, 65],
[19 , 1, 23, 75,  3, 34],
[88,  2 ,77 ,73,  7 ,63, 67],
[99, 65,  4, 28 , 6 ,16, 70 ,92],
[41 ,41 ,26, 56, 83 ,40, 80, 70, 33],
[41 ,48, 72, 33 ,47, 32 ,37 ,16, 94 ,29],
[53 ,71, 44, 65, 25, 43 ,91, 52 ,97, 51 ,14],
[70 ,11 ,33, 28, 77 ,73, 17, 78, 39, 68 ,17, 57],
[91 ,71 ,52, 38 ,17 ,14 ,91, 43 ,58, 50, 27, 29, 48],
[63, 66,  4 ,68 ,89, 53, 67 ,30 ,73, 16, 69 ,87 ,40 ,31],
[ 4 ,62 ,98 ,27 ,23 , 9 ,70, 98 ,73, 93, 38, 53, 60,  4 ,23],
]

#initializing maximumTopBot

maximumTopBot=[[]]*len(list)
for i in range(0,len(list)):
    maximumTopBot[i]=[0]*len(list[i])

for i in range(0,len(maximumTopBot[-1])):
    maximumTopBot[-1][i]=list[-1][i]
#Finding the sum for each position:
for i in range(len(maximumTopBot)-2,-1,-1):
    for j in range(0,len(maximumTopBot[i])):
        if maximumTopBot[i+1][j]>maximumTopBot[i+1][j+1]:
            maximumTopBot[i][j]=maximumTopBot[i+1][j]+list[i][j]
        else:
            maximumTopBot[i][j]=maximumTopBot[i+1][j+1]+list[i][j]

print(maximumTopBot[0][0]) #print the sum of maximum path from top to bottom