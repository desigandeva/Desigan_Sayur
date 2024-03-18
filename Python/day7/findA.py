# Problem 1
# In the input, find the first A and last A, print all the letters between these two A.
# 
# read a passage from the 'file.txt' and change to lower case
# find first a and last a using find() and rfind(), this are inbuild functions
# 
# open file and store to passage
txt_file = open("./day7/file.txt",'r')
# read a file and change to lower case
passage = txt_file.read().lower()
# find a first 'a'
first_letter = passage.find(' a ')
# find a last 'a'
last_letter = passage.rfind(' a ')
# print the letters in between first and last 'a'
print(passage[first_letter:last_letter+1])