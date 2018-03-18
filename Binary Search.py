print("Welcome to Binary Search program")

num = []

print("Enter the starting point of your list")
start = int( input() )
print("Enter the ending point of your list")
end = int( input() )

for i in range( start , end+1 ):
     num.append(int(i) )

def searchnum(start , end):
     while(True):
          
          print("Enter number that you want to search")
          search_num = int( input() )

          middle = int( (start + end ) / 2 )

          while (start <= end):
               if(search_num == middle):
                    print("Number Found at " +str(middle)+ " position")
                    break
               
               if(search_num <middle):
                    end = middle - 1

               else:
                    start = middle + 1

          option = ""
          
          if(start>end):
               print(str(search_num) + " is not available in List")

               while(True):
                    print("Would you like to search again ? :y[yes] or n[no]")
                    option = input()

                    if(option == "y" or option == "n"):
                         break
                    else:
                         print("Enter Correct Input")
                         continue

          if(option == "y"):
               continue
          else:
               exit(0)
                    
searchnum( start , end )
