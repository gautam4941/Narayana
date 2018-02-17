import functions

print("Enter the Function name that you want to use")
funcname = input()                                          #Taking Input name of Function

if(funcname == 'scan'):                                      #Scan Function to scan from a folder
    print("Do you really want to scan : y/n ?")

    if(input() == 'y'):                                     
        functions.scan(int(1) )

if(funcname == 'add'):              #Addition of 2 numbers
    print("Enter one number")
    a = int( input() )
    print("Enter one number")
    b = int( input() )
    print( str(functions.add(a,b) ) )

if(funcname == 'sub'):              #Substraction of 2 numbers
    print("Enter one number")
    a = int( input() )
    print("Enter one number")
    b = int( input() )
    print( str(functions.sub(a,b) ) )

if(funcname == 'mult'):             #Multiplicatin of 2 numbers
    print("Enter one number")
    a = int( input() )
    print("Enter one number")
    b = int( input() )    
    print( str(functions.mult(a,b) ) )

if(funcname == 'div'):              #Dvision of 2 numbers
    print("Enter one number")
    a = int( input() )
    print("Enter one number")
    b = int( input() )    
    print( str(functions.div(a,b) ) )

if(funcname == 'deletion'):             #Deletion of same file from 2 diffrent folders
    print("Enter the path of 1st Folder")
    path1 = input()                 #C:\Users\Gautam\Desktop\PYTHON\PYTHON CODES 2

    print("Enter the path of 2nd Folder")
    path2 = input()                #C:\Users\Gautam\Desktop\PYTHON\PYTHON CODES 3

    functions.deletion(path1,path2)

if(funcname == 'move'):             #To move Files from one Location to another
    print("Ready to move Files")

    while(True):
            print("Enter one file Location")
            path1 = input()         #Taking input of Location 1

            print("Enter another file Location")
            path2 = input()         #Taking input of Location 2

            functions.move(path1 , path2)   #Function for moving Files

            print("Do you want to change the Location : y/n ?")
            if( input() == 'y'):
                continue
            else:
                exit(0)

if(funcname == 'copy'):             #To move Files from one Location to another
    print("Ready to copy Files")

    while(True):
            print("Enter one file Location")
            path1 = input()         #Taking input of Location 1

            print("Enter another file Location")
            path2 = input()         #Taking input of Location 2

            functions.copy(path1 , path2)   #Function for moving Files

            print("Do you want to change the Location : y/n ?")
            if( input() == 'y'):
                continue
            else:
                exit(0)

if(funcname == 'foldercreate'):     #To Create Folders

    functions.foldercreate()        #Function to Create Folder
