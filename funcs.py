import os, re, sys, stat, datetime, time

class Fileinfo:
    '''file class: holds information and performs operations on file
        name to change what the file is called'''

    def __init__( self, filename ):
        ''' initilise file by setting oldname and new name to the file name'''
        self.oldname = filename
        self.newname = filename
        self.accesstime = os.stat(self.oldname).st_atime
        self.modtime = os.stat(self.oldname).st_mtime

    #defined string representation
    def __str__(self):
        return "Old file name: " + self.oldname + \
            "\nNew file name: " + self.newname + \
            "\nOriginal time stamp: " + str(self.accesstime) + \
            "\nNew time stamp: " + str(self.modtime)

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
        if self.accesstime != self.modtime:
            print( 'original stamp', self.accesstime, datetime.datetime.fromtimestamp( self.accesstime ))
            print( 'updated stamp', self.modtime, datetime.datetime.fromtimestamp( self.modtime ))

    def updatedatestamp( self, stamp ):
        ''' updates the date stame of the file to the user given date'''       

        #strip from new
        newdate = datetime.datetime.strptime(stamp, "%d%m%Y")
        #strip from old
        ft = os.path.getmtime(self.oldname)
        ut = datetime.datetime.fromtimestamp( ft )
        olddate = datetime.datetime.strptime( str(ut), "%Y-%m-%d %H:%M:%S.%f" )
        #create new stamp
        newdate = datetime.datetime(newdate.year, newdate.month, newdate.day, olddate.hour, olddate.minute, olddate.second)
        #save
        os.utime(self.oldname, (newdate.timestamp(), newdate.timestamp() ) )
 
    def updatetimestamp( self, stamp ):
        '''updates the timestamp of the file to the user given time'''

        #strip needed from new
        newtime = datetime.datetime.strptime(stamp, '%H%M%S')
        #proces old
        ft = os.path.getmtime(self.oldname)
        ut = datetime.datetime.fromtimestamp( ft )
        oldtime = datetime.datetime.strptime( str(ut), "%Y-%m-%d %H:%M:%S.%f" )
        #create new stamp
        newtime = datetime.datetime(oldtime.year, oldtime.month, oldtime.day, newtime.hour, newtime.minute, newtime.second)
        #save
        os.utime(self.oldname, (newtime.timestamp(), newtime.timestamp() ) )

    def updatestamp( self ):
        ''' updates the timedate stamp of the file'''
        print('update stamp')
        #os.utime( self.newname, ( self.originalstamp.timestamp(), self.oldstamp.timestamp() ) )

    def renamefile( self ):
        ''' renames the file with the given new name'''
        os.rename( self.oldname, self.newname )
        #updatestamp()

    def replace( self, oldstring, newstring):
        '''replaces old strings with new strings given by the user'''
        self.newname = re.sub(oldstring, newstring, self.newname)

    def touch( self ):
        ''' touch file, update time and date to current time and date'''
        if os.path.exists(self.oldname):
            os.utime(self.oldname, None)
        

    def trim( self, value ):
        ''' trim values off of the begging or end of the filename'''
        if value > 0:
            self.newname = self.newname[value:]
        else:
            fileParts = self.newname.split('.')
            self.newname = fileParts[0][:value] + '.' + fileParts[1]

    def upper( self ):
        ''' make the file uppercase'''
        self.newname = self.newname.upper()
