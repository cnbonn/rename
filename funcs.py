import os, re, sys, stat, datetime, time

class Fileinfo:
    '''file class: holds information and performs operations on file
        name to change what the file is called'''

    def __init__( self, filename ):
        ''' initilise file by setting oldname and new name to the file name'''
        self.oldname = filename
        self.newname = filename

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

    def printfile( self ):
        ''' prints the old name and new name of the file'''
        print( "Old Filename: ", self.oldname )
        print( "New Filename: ", self.newname )

    def updatedatestamp( self, stamp ):
        ''' updates the date stame of the file to the user given date'''
        print( "update datestamp" )

    def updatetimestamp( self, stamp ):
        '''updates the timestamp of the file to the user given time'''
        print( "update timestamp" )

    def renamefile( self ):
        ''' renames the file with the given new name'''
        os.rename( self.oldname, self.newname )

    def replace( self, oldstring, newstring):
        '''replaces old strings with new strings given by the user'''
        print( "replace" )

    def touch( self ):
        #get current time
        ct = datetime.datetime.now()
        #save current time to file
        os.utime( self.oldname, (ct.timestamp(), ct.timestamp() ) )


    def trim( self, value ):
        print( "trim" )

    def upper( self ):
        self.newname = self.newname.upper()
