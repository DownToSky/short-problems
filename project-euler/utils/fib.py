def _Fib1(n):
	"""
	Finds n-th fibonacci number using recursive function calls
	"""
	if n<0:
		raise ValueError("undefined element subscript")
	if n<=1:
		return n
	return _Fib1(n-1)+_Fib1(n-2)

def __recursive_Fib(n,fib_nums):
	if fib_nums[n] is None:
		fib_nums[n]=__recursive_Fib(n-2,fib_nums)+__recursive_Fib(n-1,fib_nums)
	return fib_nums[n]

def _Fib2(n):
	"""
	Finds n-th fibonacci number using memoization and recursive function calls
	"""
	if n<0:
		raise ValueError("undefined element subscript")
	fib_nums=[None for x in range(0,n+1)]
	if n>0:
		fib_nums[1]=1
	if n>=0:
		fib_nums[0]=0
	return __recursive_Fib(n,fib_nums)

def _Fib3(n):
	"""
	Finds n-th fibonacci number using iteration
	"""
	if n<0:
		raise ValueError("undefined element subscript")
	if n<=1:
		return n
	fn_2=0
	fn_1=1
	fn=None
	for i in range(2,n+1):
		fn=fn_2+fn_1
		fn_2=fn_1
		fn_1=fn
	return fn

def __matrix_multi(m1,m2):
	"""
	returns a matrix in form of a list of lists
	that is the multiple of m1 x m2
	assumes m1 x m2 is multiplicable and that
	m1 and m2 are in valid matrix form (list of
	lists)
	"""
	#the multiplication of a ixj matrix and a j x k matrix yields an i x k matrix
	rows=len(m1)
	columns=len(m2[1])
	m3=[[0 for j in range(0,columns)]for i in range (0,rows)]
	for i in range(0,len(m3)):
		for j in range(0,len(m3[i])):
			m1_ith_row=m1[i]
			tmp=list()
			for k in range(0,len(m2)):
				tmp.append(m2[k][j])
			m2_jth_column=tmp
			m3[i][j]=sum([m1_ith_row[t]*m2_jth_column[t] for t in range(0,len(m1_ith_row))])
	return m3

def __matrix_to_power(m,p,cache):
	if p in cache:
		return cache[p]
	elif p==1:
		cache[1]=m
		return m
	m2=__matrix_to_power(m,int(p/2),cache)
	m2=__matrix_multi(m2,m2)
	if p%2 is 1:
		m2=__matrix_multi(m2,m)
	cache[p]=m2
	return m2

def Fib(n):
	"""
	Finds the n-th fibonacci number using matrix multipication
	"""
	if n<0:
		raise ValueError("undefined element subscript")
	elif n<2:
		return n
	#Get reverse of the binary string of n in a list object. Reversing will make
	#it easier to see how multipication process works

	#bin_rep=[int(x) for x in bin(n)[2:]]
	#bin_rep.reverse()
	#powers=[2**i for i in range(0,len(bin_rep)) if bin_rep[i] is 1]
	cache=dict()
	m=[ [1,1],
		[1,0] ]
	return __matrix_to_power(m,n,cache)[0][1]

