# get a passage from input
# and call a function to revers the word

# gte input from user
passage = input("Enter a passage : ").split()

# the define reversword() function
def reversword(passage):
    # define empty list
    a = []
    for i in passage:
        a.append(i[::-1])
    return (" ".join(a))

# revers passage using lambda function
reverspassage = " ".join(map(lambda x : x[::-1],passage))
# call the reversword() function
# reverspassage = reversword(passage)
# print the revers passage
print(reverspassage)
