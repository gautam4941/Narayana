import re

mystr='send an Email 6789 from HELLO this@gmail.com To test@user.com 34 times !879'

mystr2 = '882131'

print( mystr2 )
print()
print( re.findall( '^[0-9]$', mystr2 ) )
print()
print()
print( re.findall( '^[0-9]+$', mystr2 ) )
