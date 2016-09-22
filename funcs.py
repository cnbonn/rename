import os, re, sys, stat, datetime, time

class Fileinfo:
    '''file class: holds information and performs operations on file
        name to change what the file is called'''

    def __init__( self, filename ):
        ''' initilise file by setting oldname and new name to the file name'''
        self.oldname = filename
        self.newname = filename
        self.originalstamp = os.path.getmtime( filename )
        self.newstamp = os.path.getmtime( filename )

    #defined string representation
    def __str__(self):
        return "Old file name: " + self.oldname + \
            "\nNew file name: " + self.newname + \
            "\nOriginal time stamp: " + str(self.originalstamp) + \
            "\nNew time stamp: " + str(self.newstamp)

    def countstring( self, newstring, filenum ):
        '''renames files in sequence using countstring
            #'s in count string become numbers'''
        #count number of \# in new string
        count = str(newstring).count("#")

        self.newname = re.sub("#"*count, str(filenum).zfill(count), newstring)

    def deletefile( self ):
        '''removes file from directory'''
        os.remove( self.oldname )

    def lower( self ):
        ''' converts file to lowercase'''
        self.newname = self.newname.lower()

    def printfile(self):
        ''' prints file name and file timestamp'''
        self.printfilename()
        self.printfilestamp()

    def printfilename( self ):
        ''' prints the old name and new name of the file'''
        if self.oldname != self.newname:
            print( "Old Filename: ", self.oldname )
            print( "New Filename: ", self.newname )
        else:
            print( "Filename: ", self.oldname )

    def printfilestamp( self ):
        '''prints file time stamp and changed timestamp'''
        if self.originalstamp != self.newstamp:
            print( 'original stamp', self.originalstamp, datetime.datetime.fromtimestamp( self.originalstamp ))
            print( 'updated stamp', self.newstamp, datetime.datetime.fromtimestamp( self.newstamp ))

    def updatedatestamp( self, stamp ):
        ''' updates the date stame of the file to the user given date'''
        print( "update datestamp" )
        day   = stamp[0:2]
        month = stamp[1:3]
        year  = stamp[4:]
        print( "day: ", day , " month: ", month , " year: ", year) 
    
    def updatetimestamp( self, stamp ):
        '''updates the timestamp of the file to the user given time'''
        print( "update timestamp" )
        hour = stamp[0:2]
        minute = stamp[1:3]
        second = stamp[3:]
        print( "hour: " , hour, " minute: " , minute, " second: " , second )

    def renamefile( self ):
        ''' renames the file with the given new name'''
        os.rename( self.oldname, self.newname )

    def replace( self, oldstring, newstring):
        '''replaces old strings with new strings given by the user'''
        self.newname = re.sub(oldstring, newstring, self.newname)
        print( "replace" )

    def touch( self ):
        #get current time
        ct = datetime.datetime.now()
        #save current time to file
        os.utime( self.oldname, (ct.timestamp(), ct.timestamp() ) )


    def trim( self, value ):
        if value > 0:
            self.newname = self.newname[n:]
        else:
            self.newname = self.newname[:n]

    def upper( self ):
        self.newname = self.newname.upper()
