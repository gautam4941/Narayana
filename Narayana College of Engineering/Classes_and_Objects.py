"""
class A:
    x = 5
    y = 6
    
    def add(self, a, b):
        print( 'a -> ', a )
        print( 'b -> ', b )
        print( 'self -> ', self )
        print( a + b )

    def change( self ):
        self.x = self.x+10
        self.y = self.y * 5

    def add_var( self ):
        self.z = 10
        
ob1 = A()
ob2 = A()
ob3 = A()

print( 'ob1.x -> ', ob1.x, 'ob1.y -> ', ob1.y )
print( 'ob2.x -> ', ob2.x, 'ob2.y -> ', ob2.y )
print( 'ob3.x -> ', ob3.x, 'ob3.y -> ', ob3.y )

ob1.change()
print()
print( 'ob1.x -> ', ob1.x, 'ob1.y -> ', ob1.y )
print( 'ob2.x -> ', ob2.x, 'ob2.y -> ', ob2.y )
print( 'ob3.x -> ', ob3.x, 'ob3.y -> ', ob3.y )

ob1.add_var()

print( 'ob1.z -> ', ob1.z )
print( 'ob2.z -> ', ob2.z )
print( 'ob3.z -> ', ob3.z )
"""
