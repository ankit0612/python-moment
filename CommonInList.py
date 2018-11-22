a = [1,2,1,5,6,7,8,10,11,54,26,1,5]
b = [1,5,2,6,7,84,2,3,57,1,6,9,2]

Ankit  = []

for i in a:
	if i in b:
		Ankit.append(i)
		print (Ankit)


#Another Way

a = [1,2,34,5,6,73,68,32,7,90]
b = [1,3,5,78,4,2,5,788,5,3,6,3,5,743,90]

print set(a) & set(b)
