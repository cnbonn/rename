import os, re, sys

class Fileinfo:
    '''file class: holds information and performs operations on file
        name to change what the file is called'''

    def __init__( self, filename ):
        self.oldname = filename
        self.newname = filename

    def countstring( self, newstring, filenum ):
        #count number of \# in new string
        count = str(newstring).count("#")

        self.newname = re.sub("#"*count, str(filenum).zfill(count), newstring)

    def deletefile( self ):
        os.remove( self.oldname )

    def lower( self ):
        self.newname = self.newname.lower()

    def printfile( self ):
        print( "Old Filename: ", self.oldname )
        print( "New Filename: ", self.newname )

    def updatedatestamp( self, stamp ):
        print( "update datestamp" )

    def updatetimestamp( self, stamp ):
        print( "update timestamp" )

    def renamefile( self ):
        os.rename( self.oldname, self.newname )

    def replace( self, oldstring, newstring):
        print( "replace" )

    def touch( self ):
        print( "touch" )

    def trim( self, value ):
        print( "trim" )

    def upper( self ):
        self.newname = self.newname.upper()
