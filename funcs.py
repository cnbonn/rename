import os, re, sys, stat, datetime

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
        '''removes file from directory'''
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
        ct = datetime.datetime.now()
        print( "current time: " , ct )
        
        #ft = os.path.getmtime( self.oldname )
        #print( "original", self.oldname, "mod time:", ft, time.strftime( "%m/%d/%Y %H:%M:%s", time.localtime( ft )

        #os.utime( self.oldname, (ct.timestamp(), ct.timestamp() ) )

        #gt = os.stat( self.oldname).st_mtime
        #print( "updated", self.oldname, "mod time:". gt, datetime.datetime.fromtimestamp( gt) )
        
        print( "touch" )

    def trim( self, value ):
        print( "trim" )

    def upper( self ):
        self.newname = self.newname.upper()
