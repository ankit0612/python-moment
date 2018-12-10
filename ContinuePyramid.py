def contnum(Enter): 
        
    number = 1
   
    for x in range(0, Enter): 

        for y in range(0, x+1):  
            print(number, end=" ") 
          
            number = number+1
       
        print("\r") 
  
Enter = int(input("Enter Here: "))

contnum(Enter) 
