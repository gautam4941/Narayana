list1 = []

while( True ):

    print( "Enter  one number or Type ( exit or Exit) to move out" )
    a = input()

    if( a=='exit' or a=='Exit'):
        break
    else:
        list1.append(a)

        continue

print(list1)
l = len(list1)

print( "Enter Element that you want to remove from above List" )
rem = input()

i = 0
list2 = []
list3 = []

while(i<l):

    if(rem == list1[i] ):

        list3.append(i)
        list2.append( list1.pop(i) )

        list1.insert(i, ' ')

        if(list1[i] == ' ' ):
            del list1[i]
            l = l - 1
        else:
            i = i + 1
            
    i = i + 1

l = len(list2)

print( '\n' +str(list2[0])+ " is :- " + str(l)+ " times in above List")

l = len(list3)

print('\n' +str(list2[0])+ " is at :- " )

i = 0
for i in range(l):

    print( str( list3[i] + 1 ) )

print( "Place" +'\n')

print( "Left Elements of the List are :- " +'\n')    
print(list1)

print( '\n'+ "Removed Elements from the List are :- " +'\n' )
print( list2 )
