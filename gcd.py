def gcd(a,b):
     
     if(a==0):
          return b
     if(b==0):
          return a
     if(a>b):
          return gcd(b,a%b)
     if(b>a):
          return gcd(a,b%a)
     if(a==b):
          return a
     
print("Welcome to GCD Program")

while(True):
     print("Enter one number :-")
     x = int(input())
     if(x<0):
          print("Wrong Input (Enter value is negative), please enter a new value for 1st input")
          x = int(input())
          
     print("Enter another number :-")
     y = int(input())
     if(y<0):
          print("Wrong Input (Enter value is negative), please enter a new value for 2nd input")
          y = int(input())

     print('''Would you like to find GCD on entered number or want to change the entered values :-
              Type - "go"(For gcd) or "new" (For new input)''')
     if(input() == "go"):
          print("GCD of " + str(x) + " & " + str(y) + " is :- " +str(gcd(x,y) ) )
          
          print("Would you like to exit or find a new gcd ? : y (For new GCd) / n (For exit) ")
          if(input() == "y"):
               continue
          else:
               exit(0)
     else:
          continue
