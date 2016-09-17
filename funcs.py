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

    def updatedatestamp( self ):
        print( "update datestamp" )

    def updatetimestamp( self ):
        print( "update timestamp" )

    def renamefile( self ):
        os.rename( self.oldname, self.newname )

    def replace( self ):
        print( "replace" )

    def touch( self ):
        print( "touch" )

    def upper( self ):
        self.newname = self.newname.upper()
