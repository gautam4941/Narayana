"""
a = 2
b = 3

#In Python
if( a > 0):
    print("More than 0")


#In Java
if( a >0 )
{
    print("More than 0")
}

#In Python
if( a > 0 ):
    print("More than 0")
else:
    print( "Less than 0 " )


#In Java
if( a > 0 )
{
    print("More than 0")
}
else
{
    print( "Less than 0 " )
}
"""

"""
#In Java
if( Cond1)
{
    St1....
    st2...
    ....
}
else if( Cond2)
{
    St1....
    st2...
    ....
}
else if( Cond3)
{
    St1....
    st2...
    ....
}
.
.
.
else    #Optional
{
    St1....
    st2...
    ....
}

#In Python
if( Cond1 ):
    St1....
    st2...
    ....
elif( Cond2 ):
    St1....
    st2...
    ....
elif( Cond3 ):
    St1....
    st2...
    ....
.
.
else:
    St1....
    st2...
    ....
"""

"""
a = 5
b = 14
c = 10

a_flag = ""
b_flag = ""
c_flag = ""


#find which is largest, Smallest and Middle number among a, b & c
print('a', a)
print('b', b)
print('c', c)

if( a < b ):
    if( a < c ):
        a_flag = "small"

    else:
        c_flag = "small"
        
else:
    if( b < c):
        b_flag = "small"
    else:
        c_flag = "small"


if( a > b ):
    if( a > c ):
        a_flag = "big"

    else:
        c_flag = "big"
        
else:
    if( b > c):
        b_flag = "big"
    else:
        c_flag = "big"


print( 'a_flag', a_flag )
print( 'b_flag', b_flag )
print( 'c_flag', c_flag )


if( a_flag != ""):
    if( a_flag == 'big' ):
        print( "a is the biggest among b and c" )
    else:
        print( "a is the smallest among b and c" )

else:
    print( "a is the middle value among b and c" )

if( b_flag != ""):
    if( b_flag == 'big' ):
        print( "b is the biggest among a and c" )
    else:
        print( "b is the smallest among a and c" )
else:
    print( "b is the middle value among a and c" )

if( c_flag != ""):
    if( c_flag == 'big' ):
        print( "c is the biggest among a and b" )
    else:
        print( "c is the smallest among a and b" )

else:
    print( "c is the middle value among b and a" )

"""
