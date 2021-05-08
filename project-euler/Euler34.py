#Author DownToSky
#Euler Problem 34


def is_curious(num,facts_list):
	#the sum of factorials of the digits of a negative number is positive
	if num<0:
		False	
	num=str(num)
	sum=0
	for digit in num:
		sum+=facts_list[int(digit)]
		if sum>int(num):
			return False
	if sum is int(num):
		return True
	else:
		return False

#The main point of this problem is to find an upper bound for an iteration
#Store 0 through 9 factorial
facts=[1]
for i in range(1,10):
	facts.append(facts[i-1]*i)

print(is_curious(145,facts))
