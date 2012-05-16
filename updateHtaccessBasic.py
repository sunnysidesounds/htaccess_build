#!/usr/bin/python 

import urllib2

class updateMultipleFiles(object):    

    #Set Local Path/Remote Path (true/false)
    localFile = True
    #Local Path
    getHtaccessPath = 'path_to_htaccess_you_want_to_mass_duplicate'
    #Remote Path
    getHtaccessUrl = 'your_url_here'
    #Write file (i.e. .htaccess file)
    htaccessFile = '/.htaccess'
    #List of filepath to write this file to
    htaccessFilePaths = ['path_to_put_htacess_file', 
        'path_to_put_htacess_file']
        

    def __init__(self):    
        print ''
        print '-------------------------------------------'
        print 'Update multiple .htaccess (files) at once'  
        print '(c) 2011 Jason R Alexander <sunnysidesounds@gmail.com>'
        print 'Version 1.0.0'
        print '-------------------------------------------' 
        print ''
                        
        for htaccessFiles in self.htaccessFilePaths:
            if(self.localFile):
                self.getLocalFile(self.getHtaccessPath, htaccessFiles + self.htaccessFile)
                print ' -Creating [' + self.htaccessFile + '] from local path [' + self.getHtaccessPath + ']' 
                print ' ---Putting this file in [' + htaccessFiles + ']'
            else:
                self.getRemoteFile(self.getHtaccessUrl, htaccessFiles + '/', self.htaccessFile)
                print ' -Creating [' + self.htaccessFile + '] from remote path [' + self.getHtaccessUrl + ']'
                print ' ---Putting this file in [' + htaccessFiles + ']'        
        print ''

                
    def getRemoteFile(self, remoteUrl, localPath, file):
        getRemoteUrl = urllib2.urlopen(remoteUrl)
        output = open(localPath + file,'wb')
        output.write(getRemoteUrl.read())
        output.close()    
    
    def getLocalFile(self, readPath, writePath):
        read = open(readPath,'r')
        readFile = read.read()        
        write = open(writePath,'wb')
        write.write(readFile)
        write.close() 


#updateMultipleFiles Object creation
obj = updateMultipleFiles()