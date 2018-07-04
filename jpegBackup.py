import commands as console

command = 'which '
application = 'gdrive'
# Check if gdrive is installed
output = console.getoutput(command + application)

# If its not proceed with installation
if output == '':
    print 'Installing gdrive...'

    # Download gdrive installer
    command = 'cd ~'
    console.getoutput(command)
    command = 'wget https://docs.google.com/uc?id=0B3X9GlR6EmbnWksyTEtCM0VfaFE&export=download'
    output = console.getoutput(command)

    # Extract file name of installer from output
    fileStartIndex = output.rfind('Saving to:')+14
    fileEndIndex = fileStartIndex+output[fileStartIndex:].find('\n')-3

    # Move installer to installation directory and rename to gdrive
    installFile = output[fileStartIndex:fileEndIndex]
    command = 'mv ' + installFile + ' gdrive'
    print console.getoutput(command)

    # Make installer executable and run install
    command = 'chmod +x gdrive'
    print console.getoutput(command)
    command = 'sudo install gdrive /usr/local/bin/gdrive'
    print console.getoutput(command)

    # User must finish the process by running a gdrive command and allowing acces to their google drive account
    print 'Run command "gdrive list" and finish the verification process.'
    print 'Then re-run this script to begin photo compression and google drive backup process.'
# If gdrive is installed continue
else:
    command = 'ls '
    workingDirectory = '/home'
    # Get user
    user = console.getoutput(command + workingDirectory)

    workingDirectory += ('/' + user)
    output = str(console.getoutput(command + workingDirectory))

    # Get user directories
    directories = output.split()
    # Test for archiver directory, if it doesn't exit create it
    if directories.count('photo_archiver') == 0:
        command = 'mkdir '
        destinationDirectory = workingDirectory + '/photo_archiver'
        print 'Setting up archiving directory...'
        console.getoutput(command + destinationDirectory)
        print 'Create sub-directories of photo albums inside /home/user/photo_archiver.'
        print 'Then re-run this script to compress each album and upload each archive to google drive.'
        print 'NOTE: All album sub-directories will be deleted after they are uploaded to google drive.'
        print '      If local copies are desired, be sure they exist in another directory as well.'
    # If the archive directory does exist, compress each sub-directory, upload the resulting archive to google drive,
    # and delete the archived sub-directory.
    else:
        command = 'ls '
        workingDirectory += ('/photo_archiver')
        # Get album directories to archive
        archives = console.getoutput(command + workingDirectory).split()
        for archive in archives:
            command = 'tar -zcf '
            workingDirectory += ('/' + archive)
            destinationArchive = workingDirectory + '/' + archive + '.tar.gz '
            # zip archive
            console.getoutput(command + destinationArchive + workingDirectory)

            # Upload and delete archive
            command = 'gdrive upload --delete '
            print console.getoutput(command + destinationArchive)

            # Reset working directory to archiver directory
            workingDirectory = '/home/' + user + '/photo_archiver'

            command = 'rm -r '
            trash = workingDirectory + '/' + archive
            print 'Archive uploaded. Deleting temporary folder', archive, '...'
            # Delete the album directory and everything in it
            console.getoutput(command + trash)
