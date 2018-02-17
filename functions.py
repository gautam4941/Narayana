import os                       #OS Library File to use OS Functions
import HUB

def add(x,y):                   #Addition of 2 numbers

    return x+y

def sub(x,y):                   #Substraction of 2 numbers

    return x-y

def mult(x,y):                  #Multiplication of 2 numbers

    return x*y

def div(x,y):                   #Division of 2 numbers

    return x/y


def scan(allow):

    def audioscan(Folderpath):
        filelist = []

        extensions = ["mp3" , "m4a0" , "aac"]

        allfiles = os.listdir(Folderpath)

        for extension in extensions:
            for file in allfiles:
                if extension in file:
                    filelist.append(file)

        return filelist

    def videoscan(Folderpath):
        filelist = []

        extensions = ["mp4" , "avi" , "3gp" , "mkv"]

        allfiles = os.listdir(Folderpath)

        for extension in extensions:

            for file in allfiles:
                if extension in file:
                    filelist.append(file)

        return filelist

    def imagescan(Folderpath):
        filelist = []

        extensions = ["img" , "jpg" , "png"]

        allfiles = os.listdir(Folderpath)

        for extension in extensions:

            for file in allfiles:
                if extension in file:
                    filelist.append(file)

        return filelist

    while(True):
        print("Enter the Path Location of Scan Folder :- ")
        path = input()

        print("What type of file do you want to search : image , audio , video ?")
        searchtype = input()

        list1 = []

        if(searchtype == 'audio'):
                
            list1 = audioscan(path)
            print("Would you like to print the File names : y/n ?")

            if(input() == 'y'):

                for i in list1:
                    print(i + '\n')

                print("Number of Audio Files" +str(len(list1)) )
                
                    
        if(searchtype == 'video'):
                
            list1 = videoscan(path)
            print("Would you like to print the File names : y/n ?")

            if(input() == 'y'):

                for i in list1:
                    print(i + '\n')

                print("Number of Video Files" +str(len(list1)) )

            else:

                print("Do you want to search in some other Folder : y/n ?")

                if(input() == 'n'):
                    exit(0)

        if(searchtype == 'image'):
                
            list1 = imagescan(path)
            print("Would you like to print the File names : y/n ?")

            if(input() == 'y'):

                for i in list1:
                    print(i + '\n')

                print("Number of Image Files" +str( len(list1)) )

            else:

                print("Do you want to search in some other Folder : y/n ?")

                if(input() == 'n'):
                    exit(0)

        print("Do you want to exit : y/n ?")

        if( input() == 'y'):
            exit(0)
        else:
            continue


    # Audio Path Location :- G:\MULTIMEDIA\songs

    # Video Path Location :- C:\Users\Gautam\Desktop\X-Men Series

    # Image Path Location :- G:\MULTIMEDIA\Photos\Arijit Singh

        return 0

#File Deletion from Folder :-
def deletion(a , b):
    print("Duplicate File deletion")

    while(True):
        print("Do you want to Delete the Files : y/n ?")
        decide = input()

        if(decide == 'y'):

            print("Select the folder from where you want to delete the Files : 1 or 2 ? or Enter exit to move out")
            ans = input()
            while(True):
                if( ans == '1'):
                    
                    for file in (os.listdir(a)):
                        if(file in (os.listdir(b) ) ) :
                            return os.remove( os.path.join(a, file) )
                    
                if( ans == '2'):

                    for file in (os.listdir(a)):
                        if(file in (os.listdir(b) ) ) :
                            return os.remove( os.path.join(b, file) )
                    
                if( ans == 'exit'):
                    print("Decide Again or Enter exit to Quit Program")
                    break
                else:
                    print("Enter Again , Wrong Input")
                    continue

                print("Files deleted")
        if(decide == 'n'):
            break

        else:
            print("Wrong Input , Enter Correct Input")
            continue

    return 0

def move(path1,path2):

    while(True):
        print("do you want to move file from 1st Location to 2nd or 2nd Location to 1st Location : 1/2 ?")

        if( input() == '1'):

            print("Location of Folder 1 :- " + path1)

            print("File names which are not presend in 2nd Location")

            for file in (os.listdir(path1) ):
                if ( (file in (os.listdir(path2) ) ) == False):

                    print(file +'\n')

            print("Enter the File name that you want to move from LOC1 to LOC2")
            filename = input()

            flocname1 = os.path.join(path1,filename)
            flocname2 = os.path.join(path2,filename)

            os.rename( flocname1 , flocname2 )
            print("File Moved")
            print("Would you like to move few more folders : y/n ?")
            if( input() == 'y'):
                continue
            else:
                break
        
        else:
            print("Location of Folder 2 :- " + path2)

            print("File names which are not presend in 2nd Location")

            for file in (os.listdir(path2) ):
                if ( (file in (os.listdir(path1) ) ) == False):

                    print(file +'\n')

            print("Enter the File name that you want to move from LOC2 to LOC1")
            filename = input()
            
            flocname1 = os.path.join(path1,filename)
            flocname2 = os.path.join(path2,filename)

            os.rename( flocname2 , flocname1 )

            print("File Moved")
            print("Would you like to move few more folders : y/n ?")
            if( input() == 'y'):
                continue
            else:
                break

def copy(path1,path2):
    while(True):
        print("do you want to move file from 1st Location to 2nd or 2nd Location to 1st Location : 1/2 ?")

        if( input() == '1'):

            print("Location of Folder 1 :- " + path1)

            print("File names which are not presend in 2nd Location")

            for file in (os.listdir(path1) ):
                if ( (file in (os.listdir(path2) ) ) == False):

                    print(file +'\n')

            print("Enter the File name that you want to move from LOC1 to LOC2")
            filename = input()

            flocname = os.path.join(path1,filename)

            os.copyfile( path1 , path2 )
            print("File Copied")
            
            print("Would you like to move few more folders : y/n ?")
            if( input() == 'y'):
                continue
            else:
                break
        
        else:
            print("Location of Folder 2 :- " + path2)

            print("File names which are not presend in 2nd Location")

            for file in (os.listdir(path2) ):
                if ( (file in (os.listdir(path1) ) ) == False):

                    print(file +'\n')

            print("Enter the File name that you want to move from LOC2 to LOC1")
            filename = input()
            
            flocname = os.path.join(path2,filename)

            os.copyfile( path2 , path1 )

            print("File Copied")
            
            print("Would you like to move few more folders : y/n ?")
            if( input() == 'y'):
                continue
            else:
                break

def foldercreate():
    list1 = []
    print("Folder Creation Program\n")
    count = 0

    while(True):
        print("Do you want to Create a folder : y/n ?")

        if( input() == 'y'):
            print("Enter Location Where you want to Create Folder")
            floc = input()

            print("Enter name of new Folder :- ")
            fname = input()

            fcreate = os.path.join( floc , fname )

            count = count + 1
            list1.append(fcreate)

            os.makedirs(fcreate)
        else:
            print(str(count) +" Folder Created\n")
            print("Location of folders are :- \n")

            for i in list1:
                print( i + '\n')
            break
def functionname():
     list1 = ['add' , 'sub' , 'mult' , 'div' , 'scan' , 'deletion' , 'copy' , 'move' , 'deletion' , 'foldercreate']
        
     for i in list1:
         print(i)

