sequence =  input("Enter the  words:	")
a = [i for i in sequence.split(" ")]
print (" ".join(sorted(set(a))))
