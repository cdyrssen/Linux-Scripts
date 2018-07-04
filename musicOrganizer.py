import commands as console

# This script organizes music by using an mp3 file's name. The file should be named following the convention:
#   artist[artistTag]album[albumTag]track.mp3 where [artistTag] and [albumTag] are replaced with the tags defined below

artistTag = '_artist_'
albumTag = '_album_'

workingDirectory = '/home'
command = 'ls '
user = str(console.getoutput(command + workingDirectory))
unsortedMusicDirectory = '/home/' + user + '/unsorted_music'

workingDirectory += ('/' + user)
output = str(console.getoutput(command + workingDirectory))

# get all user directories
directories = output.split()
workingDirectory = unsortedMusicDirectory
# test if an unsorted_music directory exists. if not make it
if directories.count('unsorted_music') == 0:
    command = 'mkdir '
    console.getoutput(command + workingDirectory)
    print 'Put music to be sorted in the following directory: ',
    print workingDirectory
# if an unsorted_music directory exists, then begin sorting each song in the directory
else:
    command = 'ls '
    output = str(console.getoutput(command + workingDirectory))
    # get all songs to be sorted
    unsortedSongs = output.split()

    for song in unsortedSongs:
        # artistIndex is the end of the artist's name
        artistIndex = song.find(artistTag)
        # albumIndex is the end of the album's name
        albumIndex = song.find(albumTag)
        # verify the file is an mp3 file and that the artist and albums fields aren't empty
        if song[-4:] == '.mp3' and artistIndex > 0 and albumIndex > len(artistTag)+2:
            # extract artist name
            artist = song[:artistIndex]
            # extract album name
            album = song[artistIndex+len(artistTag):albumIndex]
            # extract track name
            track = song[albumIndex+len(albumTag):-4]

            command = 'ls '
            destinationDirectory = '/home/' + user + '/Music'
            output = str(console.getoutput(command + destinationDirectory))

            # get all the artist directories
            artists = output.split()
            # test if this song's artist already has a directory. if not make one for the artist and album
            if artists.count(artist) == 0:
                command = 'mkdir '
                workingDirectory = destinationDirectory + '/' + artist
                console.getoutput(command + workingDirectory)
                workingDirectory += ('/' + album)
                console.getoutput(command + workingDirectory)

            command = 'ls '
            destinationDirectory += ('/' + artist)
            output = str(console.getoutput(command + destinationDirectory))

            # get all album directories
            albums = output.split()
            # test if the song's album already has a directory. if not make one in the artist's directory
            if albums.count(album) == 0:
                command = 'mkdir '
                workingDirectory = destinationDirectory + '/' + album
                console.getoutput(command + workingDirectory)

            command = 'mv '
            destinationDirectory = destinationDirectory + '/' + album
            source = unsortedMusicDirectory + '/' + song + ' '
            destination = destinationDirectory + '/' + track + '.mp3'
            # move and rename the song to the appropriate directory
            console.getoutput(command + source + destination)
        # if the filename doesn't match formatting requirements print message
        else:
            print 'File or filename was not in correct format for: ', song
            print 'File must be mp3 and filename must follow the convention: '
            print '\tsomeArtist'+artistTag+'artistsAlbum'+artistTag+'trackName.mp3'