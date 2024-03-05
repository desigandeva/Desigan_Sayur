# read a passage from the 'file1.txt' and change to lower case
# find first 'a' and last 'a' if 2nd a is not there find first amd last 'b'
# using find() and rfind(), this are inbuild functions
# 
# open file and store to passage
passage = open("./day7/file1.txt","r")
# read file and change to lower case
passage = passage.read().lower()

arr = ['a','b']

def findLetter(n):
    letter = arr[n]
    first_letter = passage.find(letter)
    last_letter = passage.rfind(letter)
    # return first_letter,last_letter
    if(first_letter==last_letter):
        print("2nd",arr[n],"is not there")
        findLetter(n+1)
    else:
        print(passage[first_letter:last_letter+1])

# def printLetters(first_letter,last_letter):
#     print(passage[first_letter:last_letter+1])

# first,last = findLetter('a')
# if(first==last):
#     first,last = findLetter('b')
#     if(first==last):
#         first,last = findLetter('c')
#         printLetters(first,last)
#     else:
#         printLetters(first,last)
# else:
#     printLetters(first,last)

# call the findLetter() function
findLetter(0)