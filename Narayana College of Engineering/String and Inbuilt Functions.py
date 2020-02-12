"""
msg = "Hello, How are you ?"
#index 0123456789........

print( msg )
print( msg[4] )
print( msg[5] )
print( msg[6] )
print( msg[7] )

#Slicing
#Syntax :- string_name[ start : end : incr ]
print( 'msg[ 4 : 8 : 1 ]', msg[ 4 : 8 : 1 ] )
print( 'msg[ 4 : 8 : ]', msg[ 4 : 8 : ] )
print( 'msg[  : 8 : ]', msg[  : 8 : ] )
print( 'msg[  : : ]', msg[  : : ] )
print( 'msg', msg )
"""

#Sting Inbuilt Functions

"""
#Capitalize()
#Syntax :- String_name.capitalize()

word = "hello, How are you. Hello ?"
substr = "Hello"

print( 'word', word )
print( 'substr', substr )
print( 'word.capitalize()', word.capitalize() )
print( 'substr.capitalize()', substr.capitalize() )
"""

"""
#Count how many times 5 is available in the array

In Java
count = 0
for( int i = 0 ; i < array.length ; i++ )
{
    if( array[i] == 5 )
    {
        count = count + 1
    }
}
"""

"""
#In Python

#Count()
#print( word.count( substr ) )

#Syntax :- dataset_variable/Dataset.count( character/String )
word = "Hello, How are you. Hello ?"
substr = "Hello"

print( "word.count( 'H' )", word.count( 'H' ) )
print( "substr.count( 'H' )", substr.count( 'H' ) )
print( "substr.count( 'H' )", substr.count( 'Hi' ) )
print( "word.count( 'o' )", word.count( 'o' ) )
"""

"""
#EndsWith()

word = "Hello, How are you. Hello ?"
substr1 = "Hello"
substr2 = "Hello ?"
substr3 = "lo ?"

print( 'word -> ', word )
print( 'substr1 -> ', substr1 )
print( 'substr2 -> ', substr2 )
print( 'substr3 -> ', substr3 )
print( 'word.endswith(substr1)', word.endswith(substr1) )
print( 'word.endswith(substr2)', word.endswith(substr2) )
print( 'word.endswith(substr3)', word.endswith(substr3) )

#Startwith()

print( 'word.startswith(substr1)', word.startswith(substr1) )
print( 'word.startswith(substr2)', word.startswith(substr2) )
print( 'word.startswith(substr3)', word.startswith(substr3) )
"""

"""
#find()
#Syntax :- Main_String.find(substr, location)
#If location not given, then by default location will be 0.

word = "Hello, How are you ?"
substr = "o"

print( 'word', word )
print( 'substr', substr )
firstind = word.find(substr, 0 )

print( firstind )

secondind = word.find(substr, firstind + 1 )

print( secondind )

thirdind = word.find(substr, secondind + 1)

print( thirdind )

fourthind = word.find(substr, thirdind + 1)

print( fourthind )

fifthind = word.find(substr, fourthind + 1)

print( fifthind )
"""

"""
word = "Hello,how are you ?"

print( word )           #ANS : Hello,how are you ?

print( 'word.title()', word.title() )#ANS : Hello,How Are You ?

print( 'len( word )', len( word ) )    #ANS : 19

print( 'word.upper()', word.upper() )#ANS : HELLO, HOW ARE YOU ?

print( 'word.lower()', word.lower() )#ANS : hello, how are you ?

"""

"""
#replace()
#Syntax :- Main_string.replace( old_sub_str, new_sub_str )

message = "Hello, Python Training is going on is and is"

print( 'message -> ', message )
print()
print( "message.replace( ' is', 'are' )  -> ", message.replace( ' is', 'are' ) )
print()
print( message )

message = message.replace( ' is', 'are' )
print()
print( 'message -> ', message )
"""

message = "Hello, How are you ?"

print( "message -> ", message )
print( "message.isalpha() -> ", message.isalpha() )
print( "message.isdigit() -> ", message.isdigit() )
print( "'67.8'.isdigit() -> ", '67.8'.isdigit() )
print( "'678'.isdigit() -> ", '678'.isdigit() )
print( "message.istitle() -> ", message.istitle() )
print( "message.isspace() -> ", message.isspace() )
print( "message.isalnum() -> ", message.isalnum() )
print( "'678'.isalnum() -> ", '678'.isalnum() )
print( "'678dasdad'.isalnum() -> ", '678dasdad'.isalnum() )
print( "'678dasd ad'.isalnum() -> ", '678dasd ad'.isalnum() )
print( "message.isdecimal() -> ", message.isdecimal() )
print( "'67.8'.isdecimal() -> ",'67.8'.isdecimal() )
print( "'678'.isdecimal() -> ", '678'.isdecimal() )
print( "'678'.islower() -> ", '678'.islower() )
print( 'message.islower() -> ', message.islower() )
print( "'678'.isupper() -> ", '678'.isupper() )
print( 'message.isupper() -> ', message.isupper() )
print( 'message.upper() -> ', message.upper() )
print( 'message.upper().isupper() -> ', message.upper().isupper() )
