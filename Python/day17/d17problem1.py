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
        if theatre.location==location:
            print(theatre.name)
    print()

# build function for find "Captain America" movie running theater
def findMovieTheatre(theatreList,movie):
    print('"',movie,'"'," movie running theatres :",sep='')
    for theatre in theatreList:
        if movie in theatre.getMovie():
            print(theatre.name)
    print()


lacinemas = movieTheatre('LACinemas','Madurai','Ram')
lacinemas.setMovie("Captain America")

star = movieTheatre('Star','Trichy','Kumar')
star.setMovie('Marvel')
star.setMovie('Captain America')

lotus = movieTheatre('Lotus','Madurai','Sam')
lotus.setMovie('Marvel')

giricinema = movieTheatre('GiriCinema','Madurai','Giri')
giricinema.setMovie("Captain America")

megacinema = movieTheatre('MegaCinema','Madurai','Ashwin')
megacinema.setMovie("Captain America")

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