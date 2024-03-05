# read a passage from the 'file.txt' and change to lower case
# find first a and last a using find() and rfind(), this are inbuild functions
# 
# open file and store to passage
passage = open("./day7/file.txt",'r')
# read a file and change to lower case
passage = passage.read().lower()
# find a first 'a'
first_letter = passage.find(' a ')
# find a last 'a'
second_letter = passage.rfind(' a ')
# print the letters in between first and last 'a'
print(passage[first_letter:second_letter+1])