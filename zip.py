a =[1,2,3]
strlist = ['one','two','three']
numbersTuple = ('ONE', 'TWO', 'THREE', 'FOUR')

result = zip(a,numbersTuple)
resultSet  = set(result)

result = zip(a, strlist,numbersTuple)

resultSet = set(result)
print(resultSet)