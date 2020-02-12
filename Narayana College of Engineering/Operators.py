"""
#Arithmetic Operator -> +, -, *, /, %, //, **

#Input :- Numbers
#Output Data :- Number

print( 2+3 )
print( 2-3 )
print( 2*3 )
print( 5/2 )
print( 5//2 )
print( 5%1 )
print( 15/4 )
print( 199/100 ) #Divide the both operand but shows integer part + decimal part( Deciaml Division ).
print( 199//100 ) #Divide the both operand but shows only integer part( Integer Divison ).
print( 5 * 5 )
print( 5**5 ) 
#Power Operator ( ** )
#Syntax of power( ** ) operator is ,
#base ** power
"""

"""
a = 5
b = 6
c = 5

print( f"a = { a }" )
print( f"b = { b }" )
print( f"c = { c }" )
print( f"a>b = { a>b }" )
print( f"b>a = { b>a }" )
print( f"a>c = { a>c }" )
print( f"a<c = { a<c }" )
print( f"b>c = { b>c }" )
print( f"b<c = { b<c }" )
print( f"a>=b = { a>=b }" )
print( f"a<=b = { a<=b }" )
print( f"a<=c = { a<=c }" )
print( f"a>=c = { a>=c }" )
print( f"b>=c = { b>=c }" )
print( f"b<=c = { b<=c }" )

print( f"a==b = { a==b }" )
print( f"a!= b = { a!= b }" ) 
print( f"a!=c = { a!=c }" )
print( f"a==c = { a==c }" )
print( f"b==c = { b==c }" )
print( f"b!=c = { b!=c }" )
"""

"""
a = 1
b = 2
c = 3

print(a)
print(b)
print(c)
print( ( a>b ) and (a>c) )
print( ( a>c ) and (a>b) )
print( ( b>a ) and (b>a) )
print( ( a>=b ) and (a>=c) )
print( ( a>b ) and (a<=c) )
print( ( a>=b ) and (a>c) )
print( ( a<=b ) and (a<=c) )
print( ( a==b ) and (a==c) )
print( ( a!=b ) and (a!=c) )
print( ( a!=b ) and (a==c) )
print( ( a==b ) and (a!=c) )
print( ( a<=b ) and (a<=c) )
print( ( a<=b ) and (a==c) )
print( ( a>b ) or (a>c) ) )
print( ( a>c ) or (a>b) ) )
print( ( b>a ) or (b>a) ) )
print( ( a>=b ) or (a>=c) )
print( ( a>b ) or (a<=c) )
print( ( a>=b ) or (a>c) )
print( ( a<=b ) or (a<=c) )
print( ( a==b ) or (a==c) )
print( ( a!=b ) or (a!=c) )
"""

"""
#Membership Operator -> in and not in.
#It is only applicable when we have a group or anydata type which follows indexing.
#indexing has been explained following,

name = "Hello, Training is going on"

#'H', 'e', 'l', 'l', 'o', ...
#'He', 'el', 'll', 'lo', ....
#'Hel', 'ell', ....
#index= 012345678910...
#bracket for indexing -> []

print( name )
#print( name[ 4 ] )
#print( "Hello, Buke and prashant"[4] )
#print()
print( 'H' in name )
print( 'He' in name )
print( 'llo ' in name )
print( 'llo, ' in name )
print( 'llo ' not in name )
print( 'He' not in name )
print( ',' in name )
print( 'H,' not in name )
print( ' ' in name )
print( '.' in name )
print( ',' not in name )
"""


print( id(2) )
print( id(3) )
print( id(4) )

a = 2
b = 2
c = 3

print( a )
print( b )
print( c )
print()
print( a == b )
print( a == c )
print( b == c )
print()
print( id(2) == id(3) )
print( id(2) == id(2) )
print( id(a) == id(b) )
print( id(a) == id(c) )
print( id(b) == id(c) )
print()
print( a is b )
print( a is c )
print( b is c )
print()
print( a is not b )
print( a is not c )
print( b is not c )
