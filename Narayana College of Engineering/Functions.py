"""
def a():
    for  i in range( 1, 6 ):
        print( 1 )

def b():
    for i in range( 1, 5 ):
        print( 2 )

print( a )

a = 5

print(a)
"""

"""
a = 5
b = 10

print(a)
print(b)

def f1( a, b ):
    a = a + 10
    b = b * 2

    return a, b

a, b = f1(a, b)
print( 'Outside Function1 -> ', a, b )
a, b = f1(a, b)
print( 'Outside Function2 -> ', a, b )
"""

"""
def f1(a, c, *h, **f ):
    print( 'a -> ', a)
    print( 'c -> ', c)
    print( 'h -> ', h, type(h) )
    print( 'f -> ', f, type(f) )

    print("Looping Tuple -> h,")
    for i in h:
        print( i, type(i) )

    print("Looping Dict -> f,")
    for i in f:
        print( 'key -> ', i, 'value -> ', f[i], type(i) )

f1( 2, 3, 4, 5, 6, x = True, y = 'hi')
"""

"""
def f1( a, b, *x, **y ):
    print( 'a -> ', a )
    print( 'b -> ', b )
    print( 'x -> ', x )
    print( 'y -> ', y )

    add = a+b

    for i in x:
        add = add + i

    for i in y.keys():
        add = add + y[i]

    print( "Addition = ", add )
    
f1( 2, 3, 6, 9, 2, 9, c = 6, d = 9, e = 8 )
"""
