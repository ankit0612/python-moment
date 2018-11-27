a =[1,2,3]
strlist = ['one','two','three']
numbersTuple = ('ONE', 'TWO', 'THREE', 'FOUR')

result = zip(a,numbersTuple)
resultset  = set(result)

result = zip(a, strlist,numbersTuple)

resultset = set(result)
print(resultset)
