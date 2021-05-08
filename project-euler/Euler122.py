#By DownToSky
#Euler Problem 122
from time import time

def least_exponen(pow,least_steps,l=[1]):
	"""
	We know that binary exponentiation provides us with a
	very good upper bound on the number of steps. max_h
	prompts this function to not search for levels lower than
	the value of the max_h
	"""
	if pow<1:
		raise ValueError("Exopenent should be at least 1")
	if pow==l[-1] or len(l)-1>=least_steps:
		return len(l)-1
	elif l[-1]>pow:
		return -1
	#initialize least_steps to the largest number possible
	#the number of steps is equal to pow-1. That is
	#multiplying a by itself pow-1 times
	#It's important to iterate from largest number to the least
	#since it has a higher chance of further restricting max_h
	for e in reversed(l):
		temp_list=list(l)
		temp_list.append(e+l[-1])
		steps=least_exponen(pow,least_steps,temp_list)
		if steps!=-1 and steps<least_steps:
			least_steps=steps
	return least_steps

def binary_exponen(pow):
	if pow<1:
		raise ValueError("Exopenent should be at least 1")
	if pow is 1:
		return 0
	#The number of steps required in binary exponentiation is related
	#to the binary representaion of the exponent
	#It is related to the number of digits in the bin(num)-1+number of 1's
	#except the first 1
	#e.g.
	#bin(14)=1110-> 2^3+4+2 -> 3+1+1
	bin_rep=str(bin(pow))[2:]
	steps=len(bin_rep)-1
	for dig in bin_rep[1:]:
		if dig is '1':
			steps+=1
	return steps



sum=0
for e in range(1,201):
	print(e)
	max_steps=binary_exponen(e)
	sum+=least_exponen(e,max_steps)
print(sum)
