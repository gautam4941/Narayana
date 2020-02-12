"""
#In Java
a = {  }

#In Python
a = [] or () or {}

    [] -> List
    {} -> Set, Dictionary
    () -> Tuple

"""

#a = [ 5, 6, 7, 9, 1, 0 ]

#print( a )
#print( a[3] )


#Inbuilt functions of List

#####################Data addition################
#1. append
#2. insert

"""
#append   -> Inserts the data at last
#Syntax :- list_name.append( data )
l = []

print( l )
l.append( 5 )
print( l )
l.append( 5.6 )
print( l )
l.append( True )
print( l )
l.append( 'Hi' )
print( l )
l.append( False )
print( l )
"""

"""
#insert( position, data )  -> inserts data anywhere
#Syntax :- List_name.insert( position, data )

l = []
print( l )
l.insert( 101, 5 )
print( l )
l.insert( -101, 9 )
print( l )
l.insert( 1, True )
print( l )
l.insert( 5, 'hi' )
print( l )
l.insert( 3, False )
print( l )
print( 'l[1] -> ', l[1] )
print( 'l[-1] -> ', l[-1] )
"""
"""
#Split()   ->   String to List

message = "Hello*Python Training* is going on"
print( 'message -> ', message )

splited_message = message.split( '*' )
print( "message.split( '*' ) -> ", splited_message )

#join()   ->   List to String

new_message = '$'.join( splited_message )
print()
print( 'message -> ', message )
print()
print( 'splited_message -> ', splited_message )
print()
print( 'new_message -> ', new_message )
"""

###################Data Deletion################

"""
1. del
    a) del l -> It will delete the whole list
    b) del l[index] -> It will delete given index from
                        List

2. pop()
    a) pop() -> Deletes the last value of List
    b) pop( index ) -> Deletes the given index from
                        List

3. remove( data )  -> Deletes the Given Data
"""

"""
#del
fruits = [ 'apple', 'mango', 'mango', 'cherry' ]
print( fruits )

del fruits[1]
print( "After Deletion" )
print( fruits )
"""

"""
l = [6, 7, 1, 2, 3, 1, 1, 2, 9]
print( l )

print( l.pop() )
print( "After Pop 1" )
print( l )
print( l.pop() )
print( "After Pop 2" )
print( l )
print( l.pop(2) )
print( "After Pop 3" )
print( l )
print( l.pop(1) )
print( "After Pop 4" )
print( l )
l.pop( -4 )
print( l )
"""

"""
l = [6, 7, 1, 2, 3, 1, 1, 2, 9]
print( l )
l.remove( 1 )
print( "After 1st remove" )
print( l )
l.remove( 3 )
print( "After 2nd remove" )
print( l )
l.remove( 1 )
print( "After 3rd remove" )
print( l )
l.remove( 8 )
print( "After 4th remove" )
print( l )
"""

#################Data Updation############

"""
l = [6, 7, 1, 2, 3, 1, 1, 2, 9]

print( l )
print( l[2] )
l[2] = 0
print( l )

Note:- Any DataSet( any Datatype which supports
       indexing ), If it can be changed using index
    then, It is mutable. Otherwise, Immutable

Immutability = The Process of changing the dataset
            using index but it does not changes and
            gives error is Immutability

    Ex :- msg = "Hello"
            msg[2] = 'j'
          #this will give error

Mutability = The Process of changing the dataset
            using index and it changes that index
            value is Mutability

    Ex :- l = [5, 1, 9]
          l[0] = 7
          #Then, l will be changed to [ 7, 1, 9 ]
"""

##############Extra Inbuilt Function######

"""
#index() -> same as find()

l = [6, 7, 1, 2, 3, 1, 1, 2, 9]

print( l )
print( 'l.index( 1 ) -> ', l.index( 1 ) )
print( 'l.index( 1, 0 ) -> ', l.index( 1, 0 ) )
print( 'l.index( 1, 2 ) -> ', l.index( 1, 2 ) )
print( 'l.index( 1, 3 ) -> ', l.index( 1, 3 ) )
print( 'l.index( 1, 6 ) -> ', l.index( 1, 6 ) )
print( 'l.index( 1, 7 ) -> ', l.index( 1, 7 ) )
"""

"""
#Note :- For String, always use find()
#        and for list, always use index()

#Count() -> It will work with both string and list
#EX :- string_name.count( data )
#EX :- list_name.count( data )


l = [6, 7, 1, 2, 3, 1, 1, 2, 9]
print( l )
print( 'l.count( 1 ) -> ', l.count( 1 ) )
print( 'l.count( 2 ) -> ', l.count( 2 ) )
print( 'l.count( 9 ) -> ', l.count( 9 ) )

msg = "Hello, How are you ?"

print( 'msg -> ', msg )
print( "msg.count( 'h' )-> ", msg.count( 'h' ) )
print( "msg.count( 'H' )-> ", msg.count( 'H' ) )
"""

"""
l = [ 5, 9, 1, 0, 91, 2 ]

print( l )
print( 'l.sort()' )
l.sort()
print( l )

print("Resetting the list")
l = [ 5, 9, 1, 0, 91, 2 ]
print( l )

l.sort( reverse = True )
print( "l.sort( reverse = True )" )

print( l )
print()
print("Resetting the list")
l = [ 5, 9, 1, 0, 91, 2 ]
print( l )

l.sort( reverse = False )
print( "l.sort( reverse = False )" )

print( l )
"""

"""
l = [ 5, 9, 1, 0, 91, 2 ]

print( l )
print( "After l.sort()" )
l.sort()
print( l )
print( l[ : : -1 ] )
print( "After l[ : : -1 ]" )
print( l )
l = l[ : : -1 ]
print( "l = l[ : : -1 ]" )
print( l )
"""
