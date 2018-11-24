def fact(number):
	
	if number== 0:
		return 1
	
	return number*fact(number-1)


number = int(input("Enter the number of Factorial: "))

print fact(number)
