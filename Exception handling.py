while(True):
     print("Enter 1st Number")
     a = input()
     print("Enter 2nd Number")
     b = input()

     try:                                     #try block is used to set which part of program should be under test
          if( int(a) > int(b)):
               print("1st Number is Bigger")
          else:
               print("Second Number is Bigger")
               
     except:                                 #except runs when, try function gives error
          print("You did not Enter Correct Input , Enter Integer Value")

          print("Would you like to compare numbers again ? : y/n")

          if(input() == 'y'):
               continue
          else:
               exit(0)
          
     else:                                   #else runs when there is no error
          print("2 Numbers Compared Succesfully")
          print("Would you like to compare numbers again ? : y/n")

          if(input() == 'y'):
               continue
          else:
               exit(0)
     
     finally:                                #finally runs always, even though there is error in try block.
          print("Program Executed")
