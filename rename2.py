import argparse, os, glob, re, sys

from funcs import Fileinfo

def main():
    '''main function of the program. runs main scripts'''
    args = cmdLineParse()

    filelist = filesys( args )

    runoptions( args, filelist )

    savefiles( args, filelist )


def cmdLineParse():
    '''cmaasdfd line argument parser '''
    #parse description
    parser = argparse.ArgumentParser(description="file rename application")

    #parse options mutually exclusive group
    groupCase = parser.add_mutually_exclusive_group()
    groupCase.add_argument("-l", "--lower", action="store_true",
                                        help='convert filenames to lowercase')
    groupCase.add_argument("-u", "--upper", action="store_true",
                                        help='convert filenames to uppercase')

    #parse options mutually exclusive group
    groupPrint = parser.add_mutually_exclusive_group()
    groupPrint.add_argument("-v", "--verbose", action="store_true",
                                        help='print old and new file names during processing')
    groupPrint.add_argument("-p", "--print", action="store_true",
                                        help='only print old and new filenames, do not rename')
    groupPrint.add_argument("-i", "--interactive", action="store_true",
                                        help='interactive mode, prompt user prior to processing each file')

    #parse options that are not mutually exclusive
    #options that can occur multiple times
    parser.add_argument('-t', "--trim", type=int, action='append',  metavar='N',
                                        help='positive n: trim n chars from the start of each filename\n \
                                              negative n: trim n chars from the end of each filename')
    parser.add_argument("-r", "--replace", nargs=2, type=str, action='append', metavar=('oldstring','newstring'),
                                        help='replace old string with newstring in filenames. strings \
                                              are treated as regular expressions (and generally qouted)')
    parser.add_argument("-n", "--number", nargs=1, type=str, action='store', metavar='countstring',
                                        help='renames files in sequence using countstring, #\'s in \
                                              countstring become numbers; e.g. ## becomes 01,02,..')
    #options that can not occur multiple times
    parser.add_argument("-d", "--delete", action="store_true", help='delete files')
    parser.add_argument("-dt", "--touch", action="store_true", help='\"touch\" files (update date/time stamp to current date/time)')
    parser.add_argument("-D", "--date", metavar='DDMMYYY', type=int, help='change file datestamps')
    parser.add_argument("-T", "--time", metavar='HHMMSS', type=int,  help='change file timestamps')

    #parse options required
    parser.add_argument('filename', nargs='+',   metavar='filename', help='filename(s) to perform operations on')

    #compile argument list
    args = parser.parse_args()
    
    return args    

    
def runoptions(args, filelist):
    '''runs cmd line options given by the user. runs the cmd line arguments
        in the order given by the user'''
    
    #seperate delete case 
    if args.delete:
        print("delete")
        for files in filelist:
            files.deletefile()
        return
    
    for index, files in enumerate(filelist):
        for arg in sys.argv:
            if arg in [ "-l", "--lower"]:
                files.lower()
            elif arg in [ "-u", "--upper"]:
                files.upper()
            elif arg in [ "-t", "--trim"]:
               # files.trim()

                #need to create increment system                
                print( "trim: ", args.trim )
            elif arg in [ "-r", "--replace" ]:
                files.replace(str(args.replace[0]), str(args.replace[1]))
            elif arg in ["-n", "--number" ]:
                files.countstring( str(args.number), index )
            elif arg in [ "-dt", "--touch" ]:
                print("touch")
                files.touch()
            elif arg in [ "-D", "--date" ]:
                print("date")
            elif arg in [ "-T", "--time" ]:
                print("time")
        print( "\nindex: ", index, "  file: ", files.oldname)

def savefiles(args, filelist):
    ''' goes though the list of files and saves them with there new name.'''
    #flags
    verb = False
    prnt = False
    inter = False
    if args in [ "-v" , "--verbose"]:
        verb = True
    elif args in [ "-p", "--print"]:
        prnt = True
    elif args in [ "-i", "--interactive"]:
        inter = True

    #go though files and rename 
    for files in filelist:
        if verb == True:
            files.printfile() #print files to screen
            files.renamefile()
        elif prnt == True:
            file.printfile() # print files to screen
        elif inter == True:
            files.printfile() #print file to screen
            correct = False;  #set flag to false
            while correct == False:
                choice = input( "do you want to make this change? (y/n): " )
                if choice == 'y':
                    files.renamefile()
                    correct = True # set flag to true
                elif choice == 'n':
                    correct = True #set flag to true
                else:
                    print( "invalid choice. please try again " )
            
    
def filesys(args):
    '''searches the directory for files that will be changed'''

    #initilise files
    files = args.filename

    filelist = []
   
    #go tough files and save the ones that match the naming convention 
    for s in files:
        for filename in glob.glob(s):
            filelist.append( Fileinfo( filename ) )

    return filelist



if __name__=='__main__':
    main()
