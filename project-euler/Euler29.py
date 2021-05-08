#By DownToSky
#Euler Problem 29

a_min=b_min=2
a_max=b_max=9

def divisors(num,)

#Making a dictionary of bases and their exponents
#The key is the base and the value of the key is a list of its valid exponents

pairs=dict()
for a in range(a_min,a_max+1):  # +1 for inclusiveness
    pairs[a]=set()
    for b in range(b_min,b_max+1):
        pairs[a].add(b)
#print(pairs)
#Removing the duplicate base/exponent pairs

for a in range(a_min,a_max+1):
    for b in range(b_min,b_max+1):
        if a**b in pairs:
            #print(str(a)+" "+str(b))
            for bad_elem in range(1,int(b_max/b)+1):
                #print("str:"+str(bad_elem))
                pairs[a**b].discard(bad_elem)
        
            #Then the next b is not gonna make a^b exits in pairs
            
print("After removing duplicates:\n"+str(pairs))
number_of_distinct_elems=0
for a in pairs:
    number_of_distinct_elems+=len(pairs[a])
print("\n\nThe total number of distinct elements:\n"+str(number_of_distinct_elems))

test_list=[]
for a in pairs:
    for b in pairs[a]:
        if a**b not in test_list:
            test_list.append(a**b)
        else:
            raise ValueError(str(a**b)+" already exists in pairs. a="+str(a)+" b="+str(b))