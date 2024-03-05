# You are inviting 3 of your friends over to your house for watching a movie.
# You have a list of 5 movies you like. Ask each of your friends 5 movies they like.
# List all the movies everyone likes
# List only the movies you like but no one else likes
# List the movies you like and at least one friend likes. Find which friend it is.
# List the movies all your friends like but you don't like.	

# my movies list
my_list = ["a","d","g","q","o"]

# get the movies list from 1st friend
frnd1 = list(map(lambda x: x.lower(), input("Enter 5 movies (seperate by ,) : ").split(',')))
# get the movies list from 2st friend
frnd2 = list(map(lambda x: x.lower(), input("Enter 5 movies (seperate by ,) : ").split(',')))
# get the movies list from 3st friend
frnd3 = list(map(lambda x: x.lower(), input("Enter 5 movies (seperate by ,) : ").split(',')))

# frnd1=['a', 'o', 't', 'd', 'e']
# frnd2=['a', 'p', 'e', 'm', 'z']
# frnd3=['e', 'l', 'd', 'a', 'v']
print(my_list,frnd1,frnd2,frnd3)

# common list for everyone like
com_list = []

for i in my_list:
    if i in frnd1 and i in frnd2 and i in frnd3:
        com_list.append(i)

# print everyone liked movie list
print("Movie list for everyone like :",com_list)

com_list.clear()
for i in my_list:
    if i not in frnd1 and i not in frnd2 and i not in frnd3:
        com_list.append(i)

# print movie list i like but no one like
print("Movie list for i like but no one like :",com_list)

com_list.clear()
frnd = []
for i in my_list:
    if i in frnd1:
        com_list.append(i)
        frnd.append("Friend1")
    if i in frnd2:
        frnd.append("Friend2")
        if i not in com_list:
            com_list.append(i)
    if i in frnd3:
        frnd.append("Friend3")
        if i not in com_list:
            com_list.append(i)

# print movie list i like and also atleast one friend like
print("Movie list for i and atleast one of my friend like :",com_list)
print("my friend list :",set(frnd))

com_list.clear()
for i in frnd1:
    if i in frnd2 and i in frnd3 and i not in my_list:
        com_list.append(i)

# print movie list for all my frieds like but i don't like
print("Movie list for all friends like but i don't like :",com_list)