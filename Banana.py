string= input()

vowels = 'AEIOU'

Kevin = 0
Stuart = 0
for x in range(len(string)):
    if string[x] in vowels:
        Kevin += (len(string)-x)
    else:
        Stuart += (len(string)-x)

if Kevin > Stuart:
    print ("Kevin", Kevin)
elif Kevin < Stuart:
    print ("Stuart", Stuart)
else:
    print ("Draw")