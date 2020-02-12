class Shape:        #abstract class

    def disp1(self):        #abstract function
        pass

    def disp2(self):        #abstract function
        pass

class circle( Shape ):

    def disp1(self):
        print("This is Circle")

    def disp2(self):
        print( super().disp2() )
        print("This is Disp2 of Class Circle")

class rectangle( Shape ):

    def disp1(self):
        print("This is Rectangle")

    def disp2(self):
        print( super().disp2() )            #None
        print("This is Disp2 of Class rectangle")

obc = circle()
obr = rectangle()
obs = Shape()

print( obc.disp1() )   #Done
print( obr.disp1() )    #Done
print()
obc.disp2()                 #Done
obr.disp2()                 #Done

print( obs.disp1() )
print( obs.disp2() )
