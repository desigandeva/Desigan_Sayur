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
passage = txt_file.read().replace('.','').replace(',','').replace('!','').replace('?','').lower()
# get word's seperate and stored in list using split() method
word_list = passage.split()

# assign empty list for store the 4 letter words
list_of_4_letter_word = []

# build a function for find four letter words
def findFourLetterWord(word_list):
    # strore the 4 letter words in list new_list[]
    for word in word_list:
        if len(word)==4:
            list_of_4_letter_word.append(word)
    return list_of_4_letter_word

# build a function for count the four letter words
def wordCount(word_list,count_word):
    # initialy count 0 ( for every idretion it's make 0 )
    count = 0
    # count the no of times the unique word occurred
    for word in word_list:
        if word==count_word:
            # increment the count value
            count+=1
        # print the unique word and it's count
        # print(word,":",count)
    # return count
    return count

# print the four letter word and it's count
def printWordAndCount(word_set,word_list):
    for word in word_set:
        # print the unique word and it's count
        print(word,":",wordCount(word_list,word))

# count four letter word 
def countWord(word_list):
    # initialze empty dictionary
    word_dict = {}
    # get word from word_list
    for word in word_list:
        # check length of the word is 4
        if len(word) == 4:
            # add word and word count into word_dictionary
            word_dict[word]=word_list.count(word)
    # return word_dictionary
    return word_dict

# call the function 
# countFourLetterWords(findFourLetterWord(word_list))
four_letter_word_list = findFourLetterWord(word_list)
# store the unique words in set 'word_set'
word_set = set(four_letter_word_list)
printWordAndCount(word_set,word_list)
# print(countWord(word_list))