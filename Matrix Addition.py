print("Enter 1st Matrix Data"),

print("Enter number of Rows")
row1 = int( input() )
print("Enter number of Columns")
column1 = int( input() )

matrix1 = [ [] for i in range(row1) ]

for i in range(row1):
     for j in range(column1):
          print("Enter value for Row " +str(i+1)+ " & Column " +str(j+1)+ " :- " )
          matrix1[i].append( int ( input() ) )
          
print("Enter 2nd Matrix Data"),

matrix2 = [ [] for i in range(row1) ]

for i in range(row1):
     for j in range(column1):
          print("Enter value for Row " +str(i+1)+ " & Column " +str(j+1)+ " :- " )
          matrix2[i].append( int ( input() ) )

print("Matrix1 :- ")
for i in matrix1:
     print(i)

print("Matrix2 :- ")
for i in matrix2:
     print(i)

matrix3 = [ [0 for i in range( column1 ) ] for j in range( row1 ) ]

for i in range(row1):
     for j in range(column1):

          matrix3[i][j] = matrix1[i][j] + matrix2[i][j]

print( matrix3)
