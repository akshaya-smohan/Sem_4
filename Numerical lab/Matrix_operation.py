def Matrix_add(matrix1,matrix2) :
  row = len(matrix1)
  cols = len(matrix1[0])

  result1 = [[0 for in range(cols)]for in range(row)]

  for i in range(row):
    for j in range(cols):
      result1[i][j] = matrix1[i][j] + matrix2[i][j]
  
  return result1

def Matrix_sub(matrix1,matrix2):
  row = len(matrix1)
  cols = len(matrix1[0])

  result2 = [[0 for_in range(cols)]for_in range(row)]

  for i in range(row):
    for j in range(cols):
      result2[i][j] = matrix1[i][j] - matrix2[i][j]
  
  return result2

def input_matrix(rows,cols):
  
  matrix[]

  for i in range(rows):
    row = list(map(int,input().split()))
    matrix.append(row)
  return matrix

row = int(input("Enter the number of rows : "))
cols = int(input("Enter the number of columns : "))

print("Enter the elements of the first matrix (row by row) : ")
matrix1 = input_matrix()

print("Enter the elements of the second matrix (row by row) : ")
matrix2 = input_matrix()

add_matrix = Matrix_add(matrix1,matrix2)
print("Matrix addition : ")
for i in range(row):
  for j in range(cols):
    print(add_matrix[i][j]," ")

sub_matrix = Matrix_sub(matrix1,matrix2)
print("Matrix substraction : ")
for i in range(row):
  for j in range(cols):
    print(sub_matrix[i][j]," ")


