'''
 Program: File Renaming
 Authors: Charles Bonn, Matthew De Young
 Class:   CSC 461 Programming Languages
 Instructor: Dr. Weiss
 Date: 9/22/2015
 Description: Command line instructions are processed for specific actions related
              to renaming files in the current directory, and the details of those actions
              may be displayed while they are performed if specified by user input.
 Input:  Command line arguments
 Output: Alterations to files are made as specified
 Usage:  Renaming files based on specified arguments of:
         -h --help -v --verbose -i -- interactive -l --lower -u --upper -t n --trim n -r "oldstring" "newstring" 
         --replace "oldstring" "newstring" -n "countstring" --number "countstring -p --print -d --delete 
         -dt --touch -DDMMYYYY --date DDMMYYYY -T HHMMSS --time HHMMSS files[]
'''
import argparse, os, glob, re, sys

from funcs import Fileinfo

def main():
    '''Runs the main scripts for the program.
        Description:
            The command line input is processed to generate a collection of argument data. A file list is then
            compiled for the specified arguments, and each file name undergoes the specified operations.
            Alterations are then saved to the directory if specified.
        Arguments:
            None
        Return Values:
            None
        '''
    args = cmdLineParse()

    filelist = filesys( args )

    runoptions( args, filelist )

    savefiles( args, filelist )


def cmdLineParse():
    '''Command Line Argument Parser.
        Description:
            Creating an instance of ArgumentParser, valid inputs are specified with any group specifications.
            Once all arguments are added, the argument list is returned for use by the program.
        Arguments:
            None
        Return Values:
            args: Collection of arguments specified
        '''
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
    parser.add_argument("-D", "--date", metavar='DDMMYYY', type=str, help='change file datestamps')
    parser.add_argument("-T", "--time", metavar='HHMMSS', type=str,  help='change file timestamps')

    #parse options required
    parser.add_argument('filename', nargs='+',   metavar='filename', help='filename(s) to perform operations on')

    #compile argument list
    args = parser.parse_args()
    
    return args    

def runoptions(args, filelist):
    '''Runs command line options specified by the user in the order given.
        Description:
            Initially checks if the delete option was specified, and shortcircuits evaluation if so by performing the
            operation. Otherwise the list of specified arguments is parsed in order and the specified operations are
            performed.
        Arguments:
            args: list of command line arguments
            filelist: list of files to operate upon
        Return Values:
          None
        '''
    
    #seperate delete case 
    if args.delete:
        deletefiles(args, filelist)
        quit()    # exit program
    
    for index, files in enumerate(filelist):
        trimIndex = 0
        replaceIndex = 0
        for arg in sys.argv:
            if arg in [ "-l", "--lower"]:
                files.lower()
            elif arg in [ "-u", "--upper"]:
                files.upper()
            elif arg in [ "-t", "--trim"]:
                files.trim(args.trim[trimIndex])
                trimIndex = trimIndex + 1
            elif arg in [ "-r", "--replace" ]:
                files.replace(str(args.replace[replaceIndex][0]), str(args.replace[replaceIndex][1]))
                replaceIndex = replaceIndex + 1  
            elif arg in ["-n", "--number" ]:
                files.countstring( str(args.number), index )
            elif arg in [ "-dt", "--touch" ]:
                files.touch()
            elif arg in [ "-D", "--date" ]:
                files.updatedatestamp(args.date)
            elif arg in [ "-T", "--time" ]:
                files.updatetimestamp(args.time)



def savefiles(args, filelist):
    '''Performs the renaming as specified by the user.
        Description:
            Based on the specified output type, from direct renaming to getting confirmation at each potential 
            renaming operation.
        Arguments:
            args: list of command line arguments
            filelist: list of files to operate upon
        Return Values:
            None
        '''
    #go though files and rename 
    for files in filelist:
        if args.verbose:  #verbose
            files.printfile() #print files to screen
            files.renamefile()

        elif args.print:  # print
            files.printfile() # print files to screen

        elif args.interactive: # interactive
            correct = False  #set flag to false
            while correct == False:
                files.printfile() #prints file to screen
                choice = input( "do you want to make this change? (y/n): " )
                if choice == 'y':
                    files.renamefile()
                    correct = True # set flag to true
                elif choice == 'n':
                    correct = True #set flag to true
                else:
                    print( "invalid choice. please try again " )

        else:
            files.renamefile()
           
def deletefiles(args, filelist):
    ''' delete functionality will hold print options '''
    '''Deletes files with optional output.
        Description:
            Performs file deletions, with verbose and interactive options to ensure the user does not delete
            desired files.
        Arguments:
            args: list of command line arguments
            filelist: list of files to operate upon
        Return Values:
          None
        '''
    for files in filelist:
        if args.verbose:
            files.printfile() #printfiles to screen
            files.deletefile()
        elif args.print: #print
            files.printfile()
        elif args.interactive:
            correct = False
            while correct == False:
                files.printfile()
                choice = input( "do you want to delete (y/n)?")
                if choice == 'y':
                    files.deletefile()
                    correct = True # set flag to true
                elif choice == 'n':
                    correct = True #set flag to true
                else: 
                    print( "invalid choice please try again" )
    
def filesys(args):
    '''Searches the directory for the specified files to be changed.
        Description:
            Performs globbing upon the specified file names, then ensures that the files exist before returning
            the collection.
        Arguments:
            args: list of command line arguments
        Return Values:
            filelist: list of files to operate upon
        '''
    #initilise files
    files = args.filename

    filelist = []
   
    #go tough files and save the ones that match the naming convention 
    for s in files:
        for filename in glob.glob(s):
            filelist.append( Fileinfo( filename ) )

    if not filelist:
        print( "no files matching: " , files , " in directory" )
        quit()

    return filelist



if __name__=='__main__':
    main()
