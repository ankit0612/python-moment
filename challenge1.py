def fact(i):
	if i == 0:
		return 1
	return i*fact(i-1)
i = int(raw_input("Enter the number of Factorial: "))

print fact(i)
