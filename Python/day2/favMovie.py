# Problem #4
# You are inviting 3 of your friends over to your house for watching a movie.
# You have a list of 5 movies you like. Ask each of your friends 5 movies they like.
# 
# 1. List all the movies everyone likes
# 2. List only the movies you like but no one else likes
# 3. List the movies you like and at least one friend likes. Find which friend it is.
# 4. List the movies all your friends like but you don't like.	
# 
# You are inviting 3 of your friends over to your house for watching a movie.
# You have a list of 5 movies you like. Ask each of your friends 5 movies they like.
# List all the movies everyone likes
# List only the movies you like but no one else likes
# List the movies you like and at least one friend likes. Find which friend it is.
# List the movies all your friends like but you don't like.	
# 


# my movies list
my_movie_list = ["a","d","g","q","o"]

# get the movies list from 1st friend
frnd1_movie_list = list(map(lambda x: x.lower(), input("Enter 5 movies (seperate by ,) : ").split(',')))
# get the movies list from 2st friend
frnd2_movie_list = list(map(lambda x: x.lower(), input("Enter 5 movies (seperate by ,) : ").split(',')))
# get the movies list from 3st friend
frnd3_movie_list = list(map(lambda x: x.lower(), input("Enter 5 movies (seperate by ,) : ").split(',')))

# frnd1_movie_list=['a', 'o', 't', 'd', 'e']
# frnd2_movie_list=['a', 'p', 'e', 'm', 'z']
# frnd3_movie_list=['e', 'l', 'd', 'a', 'v']
print(my_movie_list,frnd1_movie_list,frnd2_movie_list,frnd3_movie_list)

# common list for everyone like
com_movie_list = []

for movie in my_movie_list:
    if movie in frnd1_movie_list and movie in frnd2_movie_list and movie in frnd3_movie_list:
        com_movie_list.append(movie)

# print everyone liked movie list
print("Movie list for everyone like :",com_movie_list)

# clear all data stored in com_movie_list
com_movie_list.clear()

for movie in my_movie_list:
    # check movie not in frnd1_movie_list,frnd2_movie_list,frnd3_movie_list
    if movie not in frnd1_movie_list and movie not in frnd2_movie_list and movie not in frnd3_movie_list:
        # add movie to com_movie_list
        com_movie_list.append(movie)

# print movie list movie like but no one like
print("Movie list for movie like but no one like :",com_movie_list)

# clear all data stored in com_movie_list
com_movie_list.clear()
# empty frnd_list
frnd_list = []

for movie in my_movie_list:
    # check the movie in frnd1_movie_list
    if movie in frnd1_movie_list:
        # add movie to com_movie_list
        com_movie_list.append(movie)
        # add friend into frnd_list
        frnd_list.append("Friend1")
    # check the movie in frnd2_movie_list
    if movie in frnd2_movie_list:
        # add friend into frnd_list
        frnd_list.append("Friend2")
        if movie not in com_movie_list:
            # add movie to com_movie_list
            com_movie_list.append(movie)
    # check the movie in frnd3_movie_list
    if movie in frnd3_movie_list:
        # add friend into frnd_list
        frnd_list.append("Friend3")
        if movie not in com_movie_list:
            # add movie to com_movie_list
            com_movie_list.append(movie)

# print movie list movie like and also atleast one friend like
print("Movie list for movie and atleast one of my friend like :",com_movie_list)
print("my friend list :",set(frnd_list))

# clear all data stored in com_movie_list
com_movie_list.clear()

for movie in frnd1_movie_list:
    # check movie in frnd2_movie_list,frnd3_movie_list,my_movie_list
    if movie in frnd2_movie_list and movie in frnd3_movie_list and movie not in my_movie_list:
        # add movie to com_movie_list
        com_movie_list.append(movie)

# print movie list for all my frieds like but movie don't like
print("Movie list for all friends like but movie don't like :",com_movie_list)