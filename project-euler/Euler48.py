import sys



def Exponentiate(base,exp):
    if exp is 1:
        return base
    halfPower=Exponentiate(base,int(exp/2))
    ans=halfPower*halfPower
    if exp%2 == 1:
        ans= halfPower*halfPower*base
    if len(str(ans))>10:
        ans=int(str(ans)[-10:])
    return ans

s=0
for i in range(1,1001):
    s+=Exponentiate(i,i)
print (str(s)[-10:])
