# Problem #3
# From the same file as above, read from the file, count the number of unique 4 letter words and it no of occurrences
# for each word. Write this information at the end of file under the heading "Summary of 4 letter words"
# 
# For problem 2 and 3,
# Make sure your code includes exception handling for reading from a file.
# Reading material for exception handling - https://www.w3schools.com/python/python_try_except.asp
# Video https://youtu.be/83Y2qZvWxdE?si=g2MB45bZHI8-ah5q
# 
# open and read the 'file.txt'
# find the 4 letter words and count the word
# 
# 


# open the file using open() method
txt_file = open("./Python/day3/file.txt",'r')
# read file using read() method
# and remove '.' in file using replace() method
# and chnage all the words to lower case using lower() method
passage = txt_file.read().replace('.','').lower()
# get word's seperate and stored in list using split() method
word_list = passage.split()

# assign empty list for store the 4 letter words
new_list = []

# build a function for find four letter words
def findFourLetterWord(word_list):
    # strore the 4 letter words in list new_list[]
    for word in word_list:
        if len(word)==4:
            new_list.append(word)
    return new_list

# build a function for count the four letter words
def countFourLetterWords(new_list):
    # store the unique words in set 'word_set'
    word_set = set(new_list)
    # count the no of times the unique word occurred
    for word in word_set:
        # initialy count 0 ( for every idretion it's make 0 )
        count = 0
        for index in range(len(new_list)):
            if new_list[index]==word:
                # increment the count value
                count+=1
        # print the unique word and it's count
        print(word,":",count)
    return 0

# call the function 
countFourLetterWords(findFourLetterWord(word_list))
