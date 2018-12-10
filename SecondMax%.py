import pandas as pd
import numpy as np

N = input("Enter the number of Students: ")
name = input("Enter Name and Percentage here: ").split()

A = []
B = []
for i in name:
    X = i.split(",")[-1]
    Y = i.split(",")[0]
    A.append(X)
    B.append(Y)

Name = pd.DataFrame({"Name":B})
Per = pd.DataFrame({"Percentage": A})
Final = Name.join(Per)

A.sort()
if A.pop() in A:
    A.pop()
else:
    A[-1]
print(A[-1])

Final.loc[Final["Percentage"].str.contains(A[-1])]