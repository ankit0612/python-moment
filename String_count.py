listToStore = []
A = input()
for x in list(set(list(A))):
    count = 0
    for temp_x in list(A):
        if temp_x == x:
            count += 1
    listToStore.append({"Keys":x ,"count":count})
    list(listToStore)
    
    newlist = sorted(listToStore, key=lambda k: k["count"])
    
Final = newlist[::-1]
print(str(Final[0]).replace("Keys",'').replace("count",'').replace(",",'').replace("'",'').replace("[",'').replace('{','').replace("]",'').replace('}','').replace(":",''))
print(str(Final[1]).replace("Keys",'').replace("count",'').replace(",",'').replace("'",'').replace("[",'').replace('{','').replace("]",'').replace('}','').replace(":",''))
print(str(Final[2]).replace("Keys",'').replace("count",'').replace(",",'').replace("'",'').replace("[",'').replace('{','').replace("]",'').replace('}','').replace(":",''))