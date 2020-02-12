class A:
    x = 5   #Class var
    y = 6   #Class var

    def __init__(self):
        print( "Object Created -> ", self )
    
    def add(self, a, b):
        print( 'a -> ', a )
        print( 'b -> ', b )
        print( 'self -> ', self )
        print( a + b )

    def __del__(self):  #destructor, It will get called automatically when object gets destruct.
        print( "Object is Deleting -> ", self )
        
ob1 = A()
ob2 = A()
ob3 = A()
ob4 = ob1

print( 'ob1.x -> ', ob1.x, 'ob1.y -> ', ob1.y )
print( 'ob2.x -> ', ob2.x, 'ob2.y -> ', ob2.y )
print( 'ob3.x -> ', ob3.x, 'ob3.y -> ', ob3.y )

del ob2
del ob3

print( 'id(ob1) -> ', id(ob1) )
print( 'id(ob4) -> ', id(ob4) )

