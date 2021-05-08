#Author DownToSky
#Euler Problem 67

#Loads the triangle from the given file path and return a list in the following examply format:
# list=[[1],
#      [2,3],
#     [4,5,6]]
#The returbed list's element are in integer
def LoadTriangle(path):
    file = open(path,"r")
    fileContents=file.read()
    #Tokenizing with "\n" delimiter will return each level, and tokenizing the returned levels with space delims returns each element of that level
    levels=fileContents.split("\n") #Make sure that the file does not end with "\n" or the last string in levels will be empty string
    list=[[]]*len(levels)
    for i in range(0,len(levels)):
        list[i]=levels[i].split()
    #Changing the values from string to int:
    for i in range(0,len(list)):
        for j in range(0,len(list[i])):
            list[i][j]=int(list[i][j])
    return list
    
    

#For explanation refere to problem 18. This is  identical solution
list=LoadTriangle("Euler67_Triangle.txt")

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
#Notethat maximumTopBot[i][j] at this point contains the sum of numbers in the max path from
#i-th level's j-th element to the bottom level