# class for movie theatre. 
# Properties should be Name, current movie, Location, and Owner name.
# All fields except Current movie should have value.
# Add a constructor to create a new theatre.
# Add functions to change the current movie.
# 
# Each theatre needs to have a list of all the movies it played and for how long.
# The theatre owner can sell the theatre to someone else.
# They need to keep track of when the theatre was last sold and for how much money
# Write a function to list all the movies that played for more than 50 days in a given theatre.
# 
# 

# class
class movieTheatre:
    # constructor
    def __init__(self,name,location,owner):
        self.name = name
        self.location = location
        self.owner = owner
        self.sale_amount = 50000
        self.movies = {}
        # self.days = []
    # getter for owner
    def getOwner(self):
        return self.owner
    # setter for owner
    def setOwner(self,owner,amount):
        self.owner = owner
        self.sale_amount = amount
    # getter for movie
    def getMovie(self):
        return self.movies
    # setter for movie
    def setMovie(self,movie,days):
        self.movies[movie] = days

# build function for theatre in madurai
def maduraiTheatres(theatreList,location):
    print("All Theatre in "+'"'+location+'"'+" :")
    for theatre in theatreList:
        if theatre.location==location:
            print(theatre.name)
    print()
    return 0

# build function for find "Captain America" movie running theater
def findMovieTheatre(theatreList,movie):
    print('"',movie,'"'," movie running theatres :",sep='')
    for theatre in theatreList:
        if movie in theatre.getMovie().keys():
            print(theatre.name)
    print()
    return 0

# build function for find movie and running days
def movieAndDays(theatreList):
    print("List of movies and the running days in each theatre")
    for theatre in theatreList:
        print(' * '+theatre.name+' *')
        for movie,days in theatre.getMovie().items():
            print("Movie Name   : "+movie+"\nRunning Days : "+str(days))
        print()
    print()
    return 0

# build a function for seal
def saleTheatre(theatreList,oldOwner,newOwner,amount):
    print(oldOwner+" sell the theatre to "+newOwner+" at the amount of "+str(amount))
    for theater in theatreList:
        if theater.owner == oldOwner:
            print("Theatre Old Owner : "+oldOwner+"\nLast sell price : "+str(theater.sale_amount))
            theater.setOwner(newOwner,amount)
            print("Theatre New Owner : "+theater.owner+'\n'+"Sale Amount : "+str(theater.sale_amount))
    print()
    return 0

# build a function for movies are played more then some given days
def movieList(theater,gdays):
    print("In "+theater.name+" movies are played more than "+str(gdays)+" days")
    for movie,days in theater.getMovie().items():
        if days>gdays :
            print("Movie Name   : "+movie+"\nRunning Days : "+str(days))
    print()
    return 0

# LACinemas
lacinemas = movieTheatre('LACinemas','Madurai','Ram')
lacinemas.setMovie("Captain America",55)
# Star
star = movieTheatre('Star','Trichy','Kumar')
star.setMovie('Marvel',64)
star.setMovie('Captain America',55)
# Lotus
lotus = movieTheatre('Lotus','Madurai','Sam')
lotus.setMovie('Marvel',64)
# GiriCinema
giricinema = movieTheatre('GiriCinema','Madurai','Giri')
giricinema.setMovie("Captain America",55)
# MegaCinema
megacinema = movieTheatre('MegaCinema','Madurai','Ashwin')
megacinema.setMovie("Captain America",55)
# Theatre List
theatreList = []
theatreList.append(lacinemas)
theatreList.append(star)
theatreList.append(giricinema)
theatreList.append(megacinema)
theatreList.append(lotus)

# Each theatre needs to have a list of all the movies it played and for how long.
movieAndDays(theatreList)
# The theatre owner can sell the theatre to someone else.
# They need to keep track of when the theatre was last sold and for how much money
saleTheatre(theatreList,'Ram','Arun',80000)
# Write a function to list all the movies that played for more than 50 days in a given theatre.
movieList(star,50)