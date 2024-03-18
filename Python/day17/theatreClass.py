# 1. Define a class for movie theatre. 
# Properties should be Name, current movie, Location, and Owner name.
# All fields except Current movie should have value.
# Add a constructor to create a new theatre.
# Add functions to change the current movie.
# 
# In the program, creaet 5 moview theatres.
# List all the theatres in Madurai
# List all the theatres that is running the movie "Captain America"
# 
# class -> movie theatre. 
# Properties should be Name, current movie, Location, and Owner name.
# All fields except Current movie should have value.
# Add a constructor to create a new theatre.
# Add functions to change the current movie.
# 
# In the program, creaet 5 moview theatres.
# List all the theatres in Madurai
# List all the theatres that is running the movie "Captain America"
# 
# 


# class
class movieTheatre:
    # movie = []
    # constructor
    def __init__(self,name,location,owner):
        self.name = name
        self.location = location
        self.owner = owner
        self.movie = []
    # getter for movie
    def getMovie(self):
        return self.movie
    # setter for movie
    def setMovie(self,movie):
        self.movie.append(movie)

# build function for theatre in madurai
def maduraiTheatres(theatreList,location):
    print("All Theatre in "+'"'+location+'"'+" :")
    for theatre in theatreList:
        # check the theatre location in given location
        if theatre.location==location:
            # print theatre name
            print(theatre.name)
    print()

# build function for find "Captain America" movie running theater
def findMovieTheatre(theatreList,movie):
    print('"',movie,'"'," movie running theatres :",sep='')
    for theatre in theatreList:
        # check the movie running in given theatre is same as given movie
        if movie in theatre.getMovie():
            # print theatre name
            print(theatre.name)
    print()


# create object lacinemas 
lacinemas = movieTheatre('LACinemas','Madurai','Ram')
# set movie name in lacinrmas
lacinemas.setMovie("Captain America")

# create object star 
star = movieTheatre('Star','Trichy','Kumar')
# set movie name in star
star.setMovie('Marvel')
star.setMovie('Captain America')

# create object lotus 
lotus = movieTheatre('Lotus','Madurai','Sam')
# set movie name in lotus
lotus.setMovie('Marvel')

# create object giricinema 
giricinema = movieTheatre('GiriCinema','Madurai','Giri')
# set movie name in giricinema
giricinema.setMovie("Captain America")

# create object megacinema 
megacinema = movieTheatre('MegaCinema','Madurai','Ashwin')
# set movie name in megacinema
megacinema.setMovie("Captain America")

# make empty list to add theaters
theatreList = []
theatreList.append(lacinemas)
theatreList.append(star)
theatreList.append(giricinema)
theatreList.append(megacinema)
theatreList.append(lotus)

# list movies in madurai
maduraiTheatres(theatreList,'Madurai')
# list "Captain America" movie running theater
findMovieTheatre(theatreList,"Captain America")