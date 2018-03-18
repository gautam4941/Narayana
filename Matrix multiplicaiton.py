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

print("Enter number of Rows")
row2 = int( input() )
print("Enter number of Columns")
column2 = int( input() )

matrix2 = [ [] for i in range(row2) ]

for i in range(row2):
     for j in range(column2):
          print("Enter value for Row " +str(i+1)+ " & Column " +str(j+1)+ " :- " )
          matrix2[i].append( int ( input() ) )

print("Matrix1 :- ")
for i in matrix1:
     print(i)

print("Matrix2 :- ")
for i in matrix2:
     print(i)

result = [ [0 for i in range( column2 ) ] for j in range( row1 ) ]

print("Matrix after multiplicaiton :- ")

for i in range(row1):
     
   for j in range(column2):
        
       for k in range(column1):
            
           result[i][j] = matrix1[i][k] * matrix2[k][j]

for i in result:
   print(i)
