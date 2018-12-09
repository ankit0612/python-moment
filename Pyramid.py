def triangle(number): 
 
    A = 2*number-2
    for i in range(0, number): 
                     
        for B in range(0, A): 
            print(end=" ") 
      
        A = A-1
         
        for B in range(0, i+1): 
        

            print("* ", end="") 
    
        print("\r") 
  
number = int(input("Enter Here: "))
triangle(number) 
