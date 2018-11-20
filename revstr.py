def str():
	str1 = input("Enter the words :")
	if len(str1) % 4 == 0:
		return str1[::-1]
print (str())
