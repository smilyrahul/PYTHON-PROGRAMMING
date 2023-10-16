try:
    row=int(input("enter the number of rows you want to enter in a matrix\n"))
    column=int(input("enter the number of colums you want to enter in a matrix\n"))

except ValueError as e:
    print(e)

matrix1=[]
matrix2=[]
print("enter the element for the first matrix")
for i  in range(row):
    row=[]
    for j in range(column):
        temparary_storage1=input(f"enter the matrix element at row:{i+1} and column:{j+1}")
        row.append(temparary_storage1)
    matrix1.append(row)   
    
for i  in range(row):
    temparary_storage2=[]
    for j in range(column):
        value=input(f"enter the matrix element at row:{i+1} and column:{j+1} :")
        row.append(temparary_storage2)
    matrix1.append(row) 

if(matrix1!=len(matrix2)):
    print("matrix addition is not possible try to make a proper dimension matrix")

else:
    for i in range(matrix1):
