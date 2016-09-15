import argparse, os, glob

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
    parser.add_argument("-r", "--replace", nargs=2, type=str, action='append', metavar=('oldstring','newstring'),
                                        help='replace old string with newstring in filenames. strings \
                                              are treated as regular expressions (and generally qouted)')
    parser.add_argument("-n", "--number", nargs=1, type=int, action='append', metavar='countstring',
                                        help='renames files in sequence using countstring, #\'s in \
                                              countstring become numbers; e.g. ## becomes 01,02,..')
    #options that can not occur multiple times
    parser.add_argument("-d", "--delete", action="store_true", help='delete files')
    parser.add_argument("-dt", "--touch", action="store_true", help='\"touch\" files (update date/time stamp to current date/time)')
    parser.add_argument("-D", "--date", metavar='DDMMYYY', type=int, help='change file datestamps')
    parser.add_argument("-T", "--time", metavar='HHMMSS', type=int,  help='change file timestamps')

    #parse options required
    parser.add_argument('filename', nargs='+',   metavar='filename', help='filename(s) to perform operations on')

    args = parser.parse_args()

    filenames = filesys(args)
    runoptions(args, filenames)
    

    print( filenames )

def runoptions(args, filenames):
    '''runs cmd line options given by the user'''

    if args.lower:
        print ("lower")
    elif args.upper:
        print ("upper")

    if args.print:
        print ("print")
    elif args.verbose:
        print ("verbose")
    elif args.interactive:
        print ("interactive")

    if args.trim:
        trimval = args.trim
        print ("trim", trimval)

    if args.replace:
        replaceval = args.replace
        print ("replace", replaceval)

    if args.number:
        numberval = args.number
        print ("number",  numberval)

    if args.delete:
        deletefile(filenames)
        print ("delete")

    print( " ****************************" )

    for arg in vars(args):
        print (arg, getattr(args,arg))

    print( "*****************************")

   
def filesys(args):
    '''searches the directory for files that will be changed'''
    print("\ncwd:", os.getcwd())

    #initilise files
    files = args.filename
   
    for s in files:
        for filename in glob.glob(s):
            print( filename, end = ' ' )    

    print( '\n' )

    return files


def deletefile( filename ):
    ''' deletes specified file '''
    for file in filename:
        os.remove( file )

def renamefile( oldfilename, newfilename):
    '''renames current file to old file'''
    
    os.rename( oldfilename, newfilename)
    
def regexparse():
    '''handles regex expressions'''


def countstring(files, count):
    ''' count string operation. renames files with replacing ## with numbers. i.e ## is 01, 02...'''

if __name__=='__main__':
    main()
