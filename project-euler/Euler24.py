#Author DownToSky
#Euler Problem 24
import copy

#It is possible to make a tree that produces the lexicographic permutation of list
#1)Order the list
#2)Make a root and pass the ordered list to the root. The root has no value
#3)Every vertex has a number of child nodes equal to the given list's length
#4)All of the children of a vertex have a value number and an ordered list. The value number is a value given
#from the vertex's list and the ordered list of the child is found by removing the value number of that child from
#the list of the parent vertex
#5)Every child's value number is lower than that vertex's child in the right at each level, so the left most child
#has the smallest and the right most has the largest value

#Example:
#Building lexicographic tree of the list [1,2,0]
#Ordering the list: [0,1,2]
#Make root and pass the list:
#                               R[0,1,2]
#Repeat the 3-5 until there is no more childs vertecies to be made:
#(note that since the number of children is dependent on the list at each parent,
#and since the length of the list is decreasing by 1 in each leve, the height of 
#subtree's are equal to the length of the list at the root of that tree )
#                 ______________R[0,1,2]________
#                /               |              \
#               /                |               \
#           0[1,2]           1[0,2]            2[0,1]
#           /   \             |    \            |   \
#       1[2]   2[1]         0[2]    2[0]      0[1]  1[0]
#         |      |            |      |          |    |
#         2[]   1[]         2[]     0[]      1[]    0[]
#
#If we start picking the leaves of the tree from left to write and appening the parents
#of each leaf to the fron of the leaf, we will have the lexicographic permutations list:
#[[012][021][102][120][201][210]]

#Following recursive function mimic's this procedure:

#Accepts an ordered list and returns a list of permutations of the elements in the input as the output
def orderInLexicographic(orderedList):
    if len(orderedList)==1:
        return [[orderedList[0]]]
    listInLexic=[]
    for i in range(0,len(orderedList)): #Make children for this vertex equal to the length of the given ordered list
        tempList=copy.deepcopy(orderedList) #tempList will be passed to the new child
        tempNum=tempList.pop(i)         #tempNum is the value of the child
        lexicListsOfRemaining=orderInLexicographic(tempList) #This line is analougus to making a new child and its children
        for j in range(0,len(lexicListsOfRemaining)):
            listInLexic.append([tempNum]+lexicListsOfRemaining[j])
    return listInLexic


print(orderInLexicographic([0,1,2,3,4,5,6,7,8,9])[1000000-1])

