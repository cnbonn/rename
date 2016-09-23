import argparse, os, glob, re, sys
from funcs import *


def main():
    cmdLineParse()
    
def cmdLineParse():
    '''cmd line argument parser '''
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
    parser.add_argument('-r', "--replace", nargs=2, type=str,# action='append', this was nesting list in a list
                                        metavar=('oldstring','newstring'),
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
    
    argorder = sys.argv
    print( argorder )
    #get files from directory
    filenames = filesys(args)
    #populate FileInfo object
    fileObject = Fileinfo(filenames[0])
    print("File info: \n")
    print(fileObject)
    #run options
    runoptions(args, argorder, filenames)
    

    
def runoptions(args, argorder, filenames):
    '''runs cmd line options given by the user. runs the cmd line arguments
        in the order given by the user'''
    
    #seperate delete case 
    if args.delete:
        print("delete")
        deletefile(filenames)
        return
    #initialize class instance
    fileObject = Fileinfo(filenames[0])
    #go though argorder and test for cases
    for arg in argorder:
        if arg in [ "-l", "--lower"]:
            fileObject.lower()
            print("lower")
        elif arg in [ "-u", "--upper"]:
            fileObject.upper()
            print("upper")
        elif arg in [ "-t", "--trim"]:
            print("trim")
        elif arg in [ "-r", "--replace" ]:
            print(args.replace)
            fileObject.replace(args.replace[0], args.replace[1])
            print("replace")
        elif arg in ["-n", "--number" ]:
            newstring = args.number
            print("number", newstring)
            countsrting(filenames, newstring, args) 
        elif arg in [ "-dt", "--touch" ]:
            print("touch")
            touch( filenames )
        elif arg in [ "-D", "--date" ]:
            print("date")
        elif arg in [ "-T", "--time" ]:
            print("time")

    fileObject.renamefile()




'''
    print( " *****************************")
    
    print(args)

    print( " ****************************" )

    for arg in vars(args):
        print (arg, getattr(args,arg))

    print( "*****************************")
'''
   
def filesys(args):
    '''searches the directory for files that will be changed'''

    #initilise files
    files = args.filename
   
    for s in files:
        for filename in glob.glob(s):
            print( filename, end = ' ' )    

    print( '\n' )

    return files


def deletefile( filename ):
    ''' deletes specified file '''
    for files in filename:
        os.remove( files )

def renamefile( oldfilename, newfilename, args):
    '''renames current file to old file. Has options for print
        verbose and interactive modes'''
    #rename flag
    rename = True

    if args.print == True:  #print option
        rename = False
        printfile( oldfilename, newfilename)
        
    elif args.verbose == True: #verbose option
        printfile( oldfilename, newfilename)

    elif args.interactive == True: #interactive option
        print("Do you want to rename ", oldfilename, " to ", newfilename, "? (y/n)")
        userinput = input("choice: ")
        if userinput == "y":
            rename = True
        elif userinput == "n":
            rename = False
        else:
            print(" invalid option ")

    # if rename flag is true, change the file name 
    if rename == True:
        os.rename( oldfilename, newfilename)
    
def  printfile( oldfilename, newfilename ):
    ''' prints Old filename and new filename'''
    print("Old Filename: ", oldfilename)
    print("New Filename: ", newfilename)

def regexparse():
    '''handles regex expressions'''


def countstring(filename, newstring, args):
    ''' count string operation. renames files with replacing ## with numbers. i.e ## is 01, 02...'''

    #get count of number of # in newstring
    count = str(newstring).count("#") 

    #initilize count number
    num = 1

    #run though files and assign a number to each one
    for files in filename:
        #compile new name
        newname = re.sub("#"*count, str(num).zfill(count), newstring[0])
        renamefile( files, newname, args)
        num += 1

def modifydate():
    print("modifydate")

def modifytime():    
    print("modifytime")
    
def touch(filename):
    for files in filename:
        filetime = os.path.getmtime( files )
        print(filetime)
if __name__=='__main__':
    main()
