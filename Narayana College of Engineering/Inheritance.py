class A:
    a = 5
    b = 2

    def __init__(self):
        print("This is Class A constructor")

    def add(self):
        print('2+3 -> ', 2+3 )

    def disp(self):
        print("This is Disp of class A")

    def __del__(self):
        print("This is destructor of Class A")

class B( A ):

    def __init__(self):
        print( "Class B Constructor Called" )

    def add(self):
        print("This add is of Class A -> ", super().add() )
        print("This is Add of class B")

    def __del__(self):
        print( super().__del__() )
        print("This is Class B Destructor")


oba = A()
oba.add()

obb = B()
obb.add()
