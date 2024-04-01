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
list_of_4_letter_word = []

# build a function for find four letter words
def findFourLetterWord(word_list):
    # strore the 4 letter words in list new_list[]
    for word in word_list:
        # check the length of the string is 4
        if len(word)==4:
            # add the word into list_of_4_letter_word
            list_of_4_letter_word.append(word)
    # return the list_of_4_letter_word
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
    # open a file using open() method 'a' to append the data
    txt_file1 = open("./Python/day3/file.txt",'a')
    # write the summary into file
    txt_file1.write("\nSummary of 4 letter words")
    # initialy count 0
    count = 0
    # get word in word_set
    for word in word_set:
        # call wordCount() to get count of  the word
        count = wordCount(word_list,word)
        # print the unique word and it's count
        print(word,":",count)
        # write word and it's count into file
        txt_file1.write('\n'+word+"-"+str(count))

# count four letter word 
def countWord(word_list):
    # initialze empty dictionary
    word_dict = {}
    # initialy count 0
    count = 0
    # get word from word_list
    for word in word_list:
        # check length of the word is 4
        if len(word) == 4:
            # count the word
            count = word_list.count(word)
            # add word and word count into word_dictionary
            word_dict[word] = count
    # return word_dictionary
    return word_dict

# call the function 
# countFourLetterWords(findFourLetterWord(word_list))
# four_letter_word_list = findFourLetterWord(word_list)
# store the unique words in set 'word_set'
# word_set = set(four_letter_word_list)
# printWordAndCount(word_set,word_list)
# open a file using open() method 'a' to append the data
txt_file1 = open("./Python/day3/file.txt",'a')
# write the summary into file
txt_file1.write("\nSummary of 4 letter words")
# call the countWord()
word_dic = countWord(word_list)
# write the word_dic into file
txt_file1.write("\n"+str(word_dic))