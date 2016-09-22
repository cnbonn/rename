#!/usr/bin/env python3

# ***** timedate.py *****
# Python script to list and modify file date/time stamps.
# Usage: python timedate.py file1 file2 ...
# CSC461 Programming Languages, Fall 2016 (JMW)

import sys, os, time, datetime

# current time as string: YYYY-MM-DD HH:MM.SS.SSSSSS
ct = datetime.datetime.now()        
print( "current time:", ct )

# generate new time string (9/1/16 11AM, but may not get daylight savings time correct)
nt = datetime.datetime( 2016, 9, 1, 11, 0, 0 )
print( "new time:    ", nt )

# print and update file modification times
for filename in sys.argv[1:]:
    # get file mod time (in seconds since 1/1/70), convert to more useful formats (note alternate approaches)
    ft = os.path.getmtime( filename )       # or: gt = os.stat( filename ).st_mtime
    print( 'original', filename, 'mod time:', ft, datetime.datetime.fromtimestamp( ft ) )
    # or: print( 'original', filename, 'mod time:', ft, time.strftime( "%m/%d/%Y %H:%M:%S", time.localtime( ft ) ) )

    # update file mod time to 9/1/16
    os.utime( filename, ( nt.timestamp(), nt.timestamp() ) )    # timestamp() converts string to seconds

    # print new file mod time
    ft = os.path.getmtime( filename )
    print( 'updated ', filename, 'mod time:', ft, datetime.datetime.fromtimestamp( ft ) )
