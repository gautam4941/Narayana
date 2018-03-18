print("Welcome to linear Search program")

num = []

def searchnum():
     while(True):
          print("Enter number that you want to search")
          search_num = int( input() )

          if( search_num in num ):
               print( str(search_num)+" is available in List")
          else:
               print( str(search_num)+" is not available in List")

          op = ""

          while(True):
               print("\nWould you like to search again ? : y[YES] or n[NO]")
               op = input()
               
               if(op == "y" or op == "n"):
                    break
               else:
                    print("Enter correct option, ")
          if(op == "y"):
               continue
          else:
               exit(0)

def static():
     print("Enter the starting point of your list")
     start = int( input() )
     print("Enter the ending point of your list")
     end = int( input() )

     for i in range( start , end+1 ):
          num.append(int(i) )

     return num

def dynamic():
     while(True):
               print("Enter Number or enter exit to move out")
               value = input()

               if(value == "exit"):
                    break
               else:
                    num.append( int(value) )

     return num
               
while(True):
     print("Do you want to enter numbers Dynamically or static : d or s")
     op = input()

     if(op == "d"):
          dynamic()
          break
          
     elif(op=="s"):
          static()
          break
     else:
          print("Enter Correct Value\n")

if( len(num) > 0 ):
     searchnum()

else:
     print("List is Empty")
