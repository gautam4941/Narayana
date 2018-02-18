print("Welcome to Palindrome checking program")

while(True):
     
     while(True):
          print("Enter any number :- ")
          num = int(input())

          print("Would you like to proceed further or Change number ? : p(To proceed) or c(To change)")
          op = input()

          if(op == "p"):
               temp = int(num)
               newnum = 0
               remainder = 0

               while(temp != 0):

                    remainder = int(temp%10)
                    newnum = int(newnum * 10 + remainder)
                    temp = int(temp/10)

               if(newnum == num):
                    print("Number is Palindrome")
                    break
               else:
                    print("Number is not Palindrome")
                    break

          if(op == "c"):
               continue

     print("Would you like to check again ? : y(For Yes) or n(To Exit)")
     if(input() =="y"):
          continue
     else:
          exit(0)

