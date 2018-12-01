def fib():
	count = int(input(" Enter how many FIBONACCI you want to generate : "))
	i = 1
	if count == 0:
		fib = []
	elif count == 1:
		fib= [1]
	elif count == 2:
		fib ==[1,1]
	elif count > 2:
		while i < (count-1):
			fib.append(fib[i] + fib[i - 1])
			i = i + 1


	return fib
