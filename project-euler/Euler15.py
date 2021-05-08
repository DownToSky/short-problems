#Author DownToSky
#Euler Problem 15

#In intitial observation, it is possible to define a recursive function that 
#finds the number of paths from each position recursively with following definition:
#Basis:If the current position is on the right edge or the bottom edge, there is only
#one path to the final position
#Recursive step: For any other position, the number of paths to the final position 
#is the sum of number of paths from on position below and the paths in one position to the right

#For example in a 2x2 grid:
#   a00--a01--a02
#   |    |    |
#   a10--a11--a12
#   |    |    |
#   a20--a21--a22
#The number of paths from a00 to a22 is equal to number of paths from a01 to a22 plus 
#the number of paths from a10 to a22 and so on

#The main problem with this approach is that the middle positions will be calculated multiple times, and
#the larger the grid the more recalculations will happen. In the previous exqample, a11 will be calculated twice
#its value is needed to find the number of paths from a10 and also from a01 !
#This will result in a tolerable computation time for a 10x10 grid but a very bad computation time
#as the grid gets closer and closer to 20x20

#However we can avoid recalculations by allocating an (n+1)x(n+1) array and storing the values inside it
#Finds the number of paths in i and j position from the previous i and j positions
#If the current position is on the right edge or bottom edge, there is 1 path otherwise its paths in a[i+1][j]+a[i][j+1]
#So the steps for a 2x2 would be as following:
#(1)
# [unkown]  [unkown]    [1]
# [unkown]  [unkown]    [1]
#   [1]       [1]       [1]
#(2)
# [unkown]  [unkown]    [1]
# [unkown]    [2]       [1]
#   [1]       [1]       [1]
#(3)
# [unkown]    [3]       [1]
#   [3]       [2]       [1]
#   [1]       [1]       [1]
#(4)
#   [6]       [3]       [1]
#   [3]       [2]       [1]
#   [1]       [1]       [1]
#The number of paths from any position i,j is the value at that position


#The lattice is an n by n grid
n=20
grid=[[0]*(n+1)]*(n+1)

for i in range(n,-1,-1):
        for j in range(n,-1,-1):
            if i==n and j==n:
                grid[i][j]=1
            else:
                if i==n:
                    grid[i][j]=grid[i][j+1]
                else:
                    if j==n:
                        grid[i][j]=grid[i+1][j]
                    else:
                        grid[i][j]=grid[i+1][j]+grid[i][j+1]
print(grid[0][0])

#Side Note:This lattice path looks like a square section cut off of pascal's triangle:
#            1
#           1 1
#          1 2 1
#         1 3 3 1
#        1 4 6 4 1
#Which can determine the coeeficients in (a+b)^n if i recal. reeeeeeally interesting ......
