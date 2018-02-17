"""list1 = []

while(True):
    print( "Do you want to create a dictonary : y/n ?" )
    if( input() == 'y'):

        d = {}

        while(True):
            print("Enter the Key in dictionary or exit to move out")
            
            if(input() == 'exit'):
                break
            else:
                head = input()

            print("Enter the element of entered key ")
            ele = input()

            d[head] = ele

        list1.append(d)
        continue
    else:
        break

for i in list1:
    for x,y in i.items():

        print(str(x) + " :- " + str(y) )
"""
d = {}

while(True):                                                        ##Outer Dictionary
    print("Do you want to create a dictionary : y/n ?")    

    if(input() == 'y'):                                                              ## Creating Outer Dictionary
        print("Enter Title name of Key")
        key1 = input()                                                   ## Enter Key Values to Outer Dictionary

        count = 0
        a = {}
        while(True):                                                   ##Inner Dictionary
            print("Do you want to add more items :y/n ?")
            ans = input()
            
            if( ans == 'y'):
                                                                  ## Creating Inner Dictionary
                print( "Enter the title of Inner Key :- " )
                key2 = input()                                           ## Enter Key Values to Inner Dictionary
                print("Enter the values in the Recently Entered Key")
                value = input()                                         ## Enteing Values to Inner Dictionary

                a[key2] = value
            else:
                break

            d[key1] = a.keys() , a.values()
    else:
        break

print(d)



        
