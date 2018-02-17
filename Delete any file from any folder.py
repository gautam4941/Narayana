def deletion(a , b):
    print("Duplicate File deletion")

    while(True):
        print("Do you want to Delete the Files : y/n ?")

        if(input()=='y'):

            print("Enter the path of 1st Folder")
            a = input()                 #C:\Users\Gautam\Desktop\PYTHON\PYTHON CODES 2

            print("Enter the path of 2nd Folder")
            b = input()                 #C:\Users\Gautam\Desktop\PYTHON\PYTHON CODES 3

            def delete(x , y):
                for file in (os.listdir(a)):
                    if(file in (os.listdir(b) ) ) :
                        return os.remove( os.path.join(a, file) )

            print("Select the folder from where you want to delete the Files : 1 or 2 ? or Enter exit to move out")

            while(True):
                if( input()==1):
                    delete(a,b)
                    
                if( input()==2):
                    delete(b,a)

                if( input()=='exit'):
                    print("Decide Again or Enter exit to Quit Program")
                    break
                else:
                    print("Enter Again , Wrong Input")
                    continue
        if(input()=='n'):
            break

        else:
            print("Wrong Input , Enter Correct Input")
            continue
