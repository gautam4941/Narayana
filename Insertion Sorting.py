print("Welcome to Insertion Sorting program")
num = []

while(True):
     print("Enter number or Enter exit to move out")
     value = input()

     if(value=="exit"):
          break
     else:
          num.append( int(value) )

print("Before Insertion Sorting :- ")
print(num)

length = len(num)


for i in range(length):

     key = int(num[i])
     j = int(i - 1)
     
     while(j>=0 and key < num[j]):

          num[j+1] = num[j]
          j = j - 1
     num[j+1] = key

print("After Insertion Sorting :- ")
print(num)
