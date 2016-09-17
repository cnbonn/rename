import argparse, os, glob, re, sys

from funcs import Fileinfo

def main():
    args = cmdLineParse()
    
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
    
    argorder = sys.argv
    
    arginfo = [ args, argorder]
    print( arginfo )
    #get files from directory
    filenames = filesys(args)
    #run options
    #runoptions(args, argorder, filenames)
    

    
def runoptions(args, argorder, filenames):
    '''runs cmd line options given by the user. runs the cmd line arguments
        in the order given by the user'''
    
    #seperate delete case 
    if args.delete:
        print("delete")
        deletefile(filenames)
        return

    #go though argorder and test for cases
    for arg in argorder:
        if arg in [ "-l", "--lower"]:
            print("lower")
        elif arg in [ "-u", "--upper"]:
            print("upper")
        elif arg in [ "-t", "--trim"]:
            print("trim")
        elif arg in [ "-r", "--replace" ]:
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

    filelist = []
    
    for s in files:
        for filename in glob.glob(s):
            print( filename, end = ' ' )    
            filelist.append( Fileinfo( filename ) )

    print ( "*************files*****************")
    for files in filelist:
        print( files.oldname )

    print( "test" )
    filelist[0].updatedatestamp()
    print( '\n' )

    return files



def regexparse():
    '''handles regex expressions'''



    
def touch(filename):
    for files in filename:
        filetime = os.path.getmtime( files )
        print(filetime)
if __name__=='__main__':
    main()
