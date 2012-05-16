htaccess_build
==============

This mass duplicates .htaccess files across several locations. Used to block countries from multiple sites under a single VPS account.


Steps:
*	Copy your .htaccess to the included file _.htaccess
*	File out these values in updateHtaccessBasic.py

    ```
    getHtaccessPath = 'path_to_htaccess_you_want_to_mass_duplicate'
    #Remote Path
    getHtaccessUrl = 'your_url_here'
    #Write file (i.e. .htaccess file)
    htaccessFile = '/.htaccess'
    #List of filepath to write this file to
    htaccessFilePaths = ['path_to_put_htacess_file', 'path_to_put_htacess_file']
    ```
*	Login to your web server and copy these files to the root and execute. 