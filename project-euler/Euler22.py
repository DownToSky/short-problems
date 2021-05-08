#Author DownToSky
#Euler Problem 22

#Evaluates the value of the given name(written in bold)
def EvaluateName(name):
    value=0
    for i in range(0,len(name)):
        value+=ord(name[i])-64  #Character 'A' is acii 65
    return value


file = open("Euler22_names.txt","r")
fileContents=file.read()
#Generating a list of names:
nameList=[]
i=0
while i<len(fileContents):
    if fileContents[i]=="\"":
        for j in range(i+1,len(fileContents)):
            if fileContents[j]=="\"":
                nameList.append(fileContents[i+1:j])
                i=j
                break
    i+=1
nameList.sort()     #python built-in way of sorting a list of strings, regix sort would an alternative in this case
ans=0
for i in range(0,len(nameList)):
    ans+=(i+1)*EvaluateName(nameList[i])    #a name at index i is the i-th name in the list
print(ans)