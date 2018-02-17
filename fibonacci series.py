def fibo(num):

     if( num == 1):
          return 1

     if( num == 0 ):
          return 0

     if(num > 1):
          return ( fibo(num-1) + fibo(num-2) )

print( "Enter a number" )

num = int(input() )

y = num

for i in range(num):

     print( fibo(i) )

     num = num - 1

print("\nSum = " + str( fibo(y) ) )
