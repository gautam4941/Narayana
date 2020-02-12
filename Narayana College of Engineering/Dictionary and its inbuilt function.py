#        Name,S.NO, Bonus, Salary
l = [ 'Gautam', 1, 49000, 160000,
      'Rahul', 2, 60000, 130000,
      'Akash', 3, 30000, 200000]

#In List, we get the data but we don't which data is
#for what. So, we need a key which can be the represen
#-tative of data.

#Solution :- Dictionary

#In above example, we have list if are adding columns
#then, we can track that which data is for what.

"""
#Syntax :- 
x = { Key1 : value1
      ,key2 : value2
      ,.
      ,.
      ,keyn : valuen}
"""

"""
x = { 'Name' : ['Gautam', 'Akash']
      ,'sno' : [1, 2]
      ,'bonus' : [49000, 60000]
      ,'salary' : [160000, 130000]
      }

print( x )
print()
x[ 'blood_grp' ] = 'AB+'

print( x )


del x['blood_grp']
print()
print("After deleting blood group")
print( x )
print()
x['sno'].remove( 2 )
print( "After Deleting x['sno'][2]" )
print( x )
"""

"""
x = { 'Name' : ['Gautam', 'Akash']
      ,'sno' : (1, 2)
      ,'bonus' : {49000, 60000}
      ,'salary' : {'1' : [160000, 130000] }
      }

#print(x, type(x))
#print()
#print( x['salary'], type( x['salary'] ) )
#print()
#print( x['salary']['1'], type( x['salary']['1'] ) )

#x['salary']['1'].remove( 130000 )
#print( "Final Dictionary" )
#print( x )
"""

"""
x = { 'Name' : ['Gautam', 'Akash']
      ,'sno' : (1, 2)
      ,'bonus' : {49000, 60000}
      ,'salary' : {'1' : [160000, 130000] }
      }

print( 'x -> ', x )
print()
print( 'x.keys() -> ', x.keys() )
print()
print( 'x.values() -> ', x.values() )
print()
print( 'x.items() -> ',x.items() )
"""

x = { 'Name' : ['Gautam', 'Akash']
      ,'sno' : (1, 2)
      ,'bonus' : {49000, 60000}
      ,'salary' : {'1' : [160000, 130000] }
      }

"""
print( x.keys() )

x_keys = list( x.keys() )

print( x_keys, type( x_keys ) )    

print( 'len(x_keys) -> ', len(x_keys) )

for i in range(0, len(x_keys) ):
    print( i, x_keys[i], x[ x_keys[i] ] )
"""
print(x)
print()
for i in x.keys():
    print( i, x[i] )
