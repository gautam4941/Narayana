print("Welcome to Buuble Sort")
num = []

while(True):
     print("Enter number or Enter exit to move out")
     value = input()

     if(value=="exit"):
          break
     else:
          num.append( int(value) )

print("Before Bubble Sorting :- ")
print(num)

length = len(num)

for i in range(length):
     for j in range(length-i-1):

          if( num[j] > num[j+1]):
               temp = num[j]
               num[j] = num[j+1]
               num[j+1] = temp

print("After Bubble Sorting :-")
print(num)
