"""
a = [ ]
t = ()

print( a, type(a) )
print( t, type(t) )

a = [ 5, 9, 8, 1 ]
t = ( 5, 9, 8, 1 )


print( a, type(a) )
print( t, type(t) )
"""

"""
x = ( 5, 9, 1, 0, 1, 2 )

print( x )

#x.append( 7 )

#x.pop()

#x.remove( 1 )

#del x[2]

#x[2] = 0   #tuple is immutable

#x.sort()

print( 'x.count( 1 ) -> ',x.count( 1 ) )       #2

print( 'x.index( 1 ) -> ', x.index( 1 ) )       #2
print( 'x.index( 1 ) -> ', x.index( 1, 3 ) )    #4

print( x )

"""

"""
#O/P:-

#( 5, 6, 1, 2 )
#( 5, 9, 1, 7, 9 )


t = ( 5, 6, 1, 2 )
print( t )
t = list(t)
print( t )
t[ 1 ] = 9
t[ 3 ] = 7
print( t )
t.append( 9 )
print( t )
t = tuple(t)
print( t )
"""
