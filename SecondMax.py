A = input("Enter here: ").split()

A.sort()
A.pop()
if A.pop() in A:
    A.pop()
else:
	A[-1]

print(A[-1])
