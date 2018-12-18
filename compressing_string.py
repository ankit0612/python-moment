sub_str = 0
string = input()
while sub_str in range(len(string)):
    temp = string[sub_str]
    k = sub_str+1
    count = 1
    while k<len(string):
        if string[k] != temp:
            break
        count = count+1
        k = k+1
    
    print((count,int(string[sub_str])))
    sub_str = k