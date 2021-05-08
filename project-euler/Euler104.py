from utils import fib

def is_pandigital(digits):
	nums={1,2,3,4,5,6,7,8,9}
	if len(digits) is not 9:
		raise ValueError("is_pandigital requires a list of 9 numbers")
	for digit in digits:
		if digit in nums:
			nums.remove(digit)
		else:
			return False
	return True

index=1
fn_2=0
fn_1=1
while True:
	index+=1
	fn=int(str(fn_1+fn_2)[-9:])
	fn_2=fn_1
	fn_1=fn
	if index%1000==0:
		print(fn)
	str_f=str(fn)
	if len(str_f)<9:
		continue
	str_digits=str_f[-9:]
	digits=[int(c) for c in str_digits]	
	if is_pandigital(digits):
		str_digits=str(fib.Fib(index))[:9]
		digits=[int(c) for c in str_digits]
		if is_pandigital(digits):
			print(index)
			break

