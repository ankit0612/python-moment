number = int(input("Enter Number here:  "))

for dict in range(0,number):
    
    num = 1
    
    for j in range(0, dict+1):
        
        print({num:num*num}, end=" ")
        
        num = num +1
        
    print("\r")
