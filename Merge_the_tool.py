String  = input("Enter Here : ")
Chunks = int(input("Enter the number of chunks you want: "))
Split_by = int(len(String)/Chunks)
ref = 0
for chunks in range(0,Split_by):
#     print(String[ref:Split_by])
    print("".join(set(String[ref:Split_by])))
    ref = Split_by
    Split_by += Split_by
    
#     print("".join(set(String[ref:n])))