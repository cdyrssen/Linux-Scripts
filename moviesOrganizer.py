import commands as console

# This script seperates movies into different directories based on their genre.
# Movies that should be shorted need to be .avi format and be located in the userss unsorted_movies directory
# Sorted movies are put into the user's Movies directory
# Unsorted movies should follow the naming convention movieGenre[genreTag]movieTitle.avi where [genreTag] is the string
# genreTag below

genreTag = '_genre_'

workingDirectory = '/home'
command = 'ls '
# get user directory
user = str(console.getoutput(command + workingDirectory))
unsortedMoviesDirectory = '/home/' + user + '/unsorted_movies'

workingDirectory += ('/' + user)
output = str(console.getoutput(command + workingDirectory))

# get all user directories in a list
directories = output.split()
# if running the script for the first time, the unsorted_movies and Movies directories need to be created
if directories.count('unsorted_movies') == 0:
    command = 'mkdir '
    console.getoutput(command + unsortedMoviesDirectory)
    print 'Put movies to be sorted in the following directory: ',
    print unsortedMoviesDirectory

    workingDirectory += '/Movies'
    if directories.count('Movies' == 0):
        console.getoutput(command + workingDirectory)
        print 'The directories of sorted movies is in the following directory: ',
        print workingDirectory
# if not then begin sorting movies in the /home/user/unsorted_movies directory
else:
    command = 'ls '
    output = str(console.getoutput(command + workingDirectory))
    # get all files in the unorsted_movies directory
    unsortedMovies = output.split()

    # sort each movie file
    for movie in unsortedMovies:
        # genreIndex marks the end of the movie's genre
        genreIndex = movie.find(genreTag)
        # verify the file is .avi format and there is a genre for the movie to be sorted into
        if movie[-4:] == '.avi' and genreIndex > 0:
            genre = movie[:genreIndex]
            title = movie[genreIndex+len(genreTag):-4]

            command = 'ls '
            workingDirectory = '/home/' + user + '/Movies'
            output = str(console.getoutput(command + workingDirectory))

            destinationDirectory = workingDirectory + '/' + genre
            # get all genres
            genres = output.split()
            # test if current genre exists. if not make a new directory
            if genres.count(genre) == 0:
                command = 'mkdir '
                console.getoutput(command + destinationDirectory)

            # move and rename file to appropriate directory
            command = 'mv '
            source = unsortedMoviesDirectory + '/' + movie + ' '
            destination = destinationDirectory + '/' + title + '.avi'
            console.getoutput(command + source + destination)

        # file did not meet requirments. print message
        else:
            print 'File or filename was not in correct format for: ', movie
            print 'File must be avi and filename must follow the convention: '
            print '\tsomeGenre'+genreTag+'movieTitle.avi'