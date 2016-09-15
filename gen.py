
import argparse, os, glob

sub = [".txt" , ".os", ".mpp", ".xkcd", ".file"]
pre = ["man", "bob", "rawr", "snap", "rabble" ]
required = ["README.md" , "rename.py", "gen.py" , ".git"]

def main():
    cmdLineParse()

def cmdLineParse():
    ''' cmd line parse of options'''
    parser = argparse.ArgumentParser(description="gen for rename")
    
    case = parser.add_mutually_exclusive_group()
    case.add_argument("-c", "--create", action="store_true",
                                        help='create files for rename')
    case.add_argument("-r", "--remove", action="store_true",
                                        help='delete files created for rename')
    case.add_argument("-k", "--clean", action="store_true",
                                        help='clean files ( keep required files )')
    args = parser.parse_args()
    runoptions(args)

def runoptions(args):
    '''run options given by the user'''
    
    if args.create:
        create()
    elif args.remove:
        remove()
    elif args.clean:
        clean()

def clean():
    '''cleans all files that are not listed in the required files list from the directory'''
    filelist = os.listdir()

    for files in filelist:
        dndflag = False # dont delete flag
        for i in required:
            if i == files:
                dndflag = True
        if dndflag != True:
            os.remove( files ) 

def create():
    ''' create files '''
        
    for i in pre:
        for j in sub:
            file = str(i) + str(j)
            tfile = open( file , 'w')
            tfile.close()
            print ( "creating: ", file )
    print("files created")

def remove():
    ''' remove files created '''

    for i in pre:
        for j in sub:
            file = str(i) + str(j)
            os.remove( file )

    print( "files removed" ) 

if __name__=='__main__':
    main()       
