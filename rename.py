import argparse

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
parser.add_argument('-t', "--trim", type=int, metavar='N',
                                        help='positive n: trim n chars from the start of each filename\n \
                                              negative n: trim n chars from the end of each filename')
parser.add_argument("-r", "--replace", nargs=2, type=str, metavar=('oldstring','newstring'),
                                        help='replace old string with newstring in filenames. strings \
                                              are treated as regular expressions (and generally qouted)')
parser.add_argument("-n", "--number", nargs=1, type=int, metavar='countstring',
                                        help='renames files in sequence using countstring, #\'s in \
                                              countstring become numbers; e.g. ## becomes 01,02,..')
parser.add_argument("-d", "--delete", action="store_true", help='delete files')
parser.add_argument("-dt", "--touch", action="store_true", help='\"touch\" files (update date/time stamp to current date/time)')
parser.add_argument("-D", "--date", metavar='DDMMYYY', help='change file datestamps')
parser.add_argument("-T", "--time", metavar='HHMMSS', help='change file timestamps')

#parse options required
parser.add_argument('filename', nargs='*', metavar='filename', help='filename(s) to perform operations on')

args = parser.parse_args()


if args.lower:
    print ("lower")
elif args.upper:
    print ("upper")
else:
    print (none)
    
nb = args.trim #parser.parse_args()
print(nb)
    
ns = args.filename #parser.parse_args()
print(ns)
