coordinate = ['x', 'y', 'z']
value = [3, 4, 5, 0, 9]

result = zip(coordinate, value)
resultlist = list(result)
print (resultlist)

c,v = zip(*resultlist)

print('c =', c)

print('v = ', v)