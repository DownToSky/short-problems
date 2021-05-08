#Author DownToSky
#Euler Problem 126

#Returns the number of cubes used to cover the surface of 
#the cuboid with the specified dimension and layer
#Justification of the formula used 
def CubesInLayer(x,y,z,l):
    if l==1:
        return 2*(x*y+x*z+y*z)
    else:
        return 2*(x*y+x*z+y*z)+4*(x+y+z)*(l-1)+4*(l-1)*(l-2) #To skip int parsing write 8/2 as 4

cap=20000    #80000        
C=[0]*(cap)

x=1
while CubesInLayer(x,x,x,1)<cap:
    y=x
    while CubesInLayer(x,y,y,1)<cap:
        z=y
        while CubesInLayer(x,y,z,1)<cap:
            l=1
            while CubesInLayer(x,y,z,l)<cap:
                C[CubesInLayer(x,y,z,l)]+=1
                l+=1
            z+=1
        y+=1
    x+=1

for i in range(1,len(C)):
    if C[i]==1000:
        print(i)
        break
