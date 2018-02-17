#! python3
import math

print( "Enter any number" )

num = input()

num1 = int(num)

print( " You have Entered :- " +num)

l = len( num )

num = int( num )
list1 = []

i = 0

while(i < l):

    b = int ( num /(math.pow(10, (l-(i+1) ) ) ))

    list1.insert(i,b)

    num = int(num % ( math.pow(10, (l-(i+1)) ) ) )

    print(list1[i])

    i = i + 1

i = 0

list2 = []

while(i < l):

        b = int(list1[i] * (math.pow(10, (l-(i+1) ) ) ) )

        list2.insert(i,b)
        
        print(list2[i])

        i = i + 1

i = 0

list3 = []

while( i < l ):

    fact = 1

    while( num1 >= list2[i] ):

        fact = fact * num1
        num1 = num1 - 1

    if( num1 <10 and num>=1 ) :
        fact = fact * num1
        num1 = num1 - 1
        
    list3.insert(i,fact)

m  = 1

while(i<l):
    m = list3[i] * m
    i = i + 1

print("Factorial of number " + num1 + " is :- " + m )
