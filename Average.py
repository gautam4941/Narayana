print("Welcome to Average Program")
num = []

while(True):
     print("Enter value or Enter exit to move out")
     value = input()

     if(value == "exit"):
          break
     else:
          num.append(int(value))

l = int( len( num ) )
total = int(0)

for i in num:
     total = total + i

average = float( total / l )

print("Average of ")
for i in num:
     print(i)

print("is :- " +str(average))







          
