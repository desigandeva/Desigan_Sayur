# Problem #1
# write a program that reads a passage and reverses the order of 
# letters in each word while keeping the word order intact. Use function.
# Eg- input - I am Sayur, good.
# Output I ma ruyaS
# 
# get a passage from input
# and call a function to revers the word
# 

# get input from user
word_list = input("Enter a passage : ").split()

# the define reversword() function
def reversword(word_list):
    # define empty list
    new_list = []
    # gte word from word_list
    for word in word_list:
        # check if any ,.?! in end of the string
        if word[-1]==',' or word[-1]=='.' or word[-1]=='!' or word[-1]=='?':
            # only revers the word and then add char end of the word
            new_list.append(word[-2::-1]+word[-1])
        # else
        else:
            # change the word into revers order and add to new_list
            new_list.append(word[::-1])
    # return new_list as string
    return (" ".join(new_list))

# revers passage using lambda function
# reverspassage = " ".join(map(lambda x : x[::-1],word_list))
# call the reversword() function
reverspassage = reversword(word_list)
# print the revers passage
print(reverspassage)
