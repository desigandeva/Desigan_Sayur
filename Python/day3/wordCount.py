# Problem #2
# Read a passage from a file. 
# Count the number of times the word 'the' followed by another 'the' without 'a' in between.
# 
# Eg:- The king went to the forest with the wife and a servernt. The king shot a deer. The king went to the forest again the next day.
# answer is 4 (The king, the forest, The King the next).
# 
# read the passage from file
# 

# open file using open module 
txt_file = open("./Python/day3/file.txt","r")
# read file using read() method
# and remove '.' in file using replace() method
# and chnage all the words to lower case using lower() method
passage = txt_file.read().replace('.','').lower()
# get word's seperate and stored in list using split() method
word_list = passage.split()


# build a function to count a word
def countWord(word_list,input_word):
    # initialize count as 0
    count = 0
    # create empty list
    new_list = []
    # create empty string 
    # previousWord =''
    # for loop for find "the","a" and 'a' in any word
    # for index in range(len(word_list)):
    #     # find "the" or "a" in word_list
    #     if (word_list[index]==input_word):
    #         previousWord = input_word
    #         if(previousWord == input_word ):
    #             count = count + 1      
    #     elif ('a' in word_list[index]):
    #         previousWord = 'a'
    # for loop for find "the","a" and 'a' in any word
    for index in range(len(word_list)):
        # find "the" or "a" in word_list
        if (word_list[index]==input_word) or ('a' in word_list[index]):
            # add word into new_list
            new_list.append(word_list[index])
    # for loop for find "the" followed by another "the"
    # for index in range(len(new_list)-1):
            if len(new_list) >= 2 and new_list[-2] == input_word and new_list[-1] == input_word:
                    count += 1
            # find the word "the" followed by another "the"
        # if new_list[index]==new_list[index+1] and new_list[index+1]==input_word:
            # increment the count
            # count += 1
    # print count
    # print("Count of 'the' followed by another 'the' is : ",count)
    return count

# build a function to count a word
def wordCount(word_list,word):
    # initialize count as 0
    count = 0
    # initialize total_count as 0
    total_count = 0
    # initialize index as 0
    index = 0
    # initialize new_index as 0
    new_index = 0
    # set status check point
    status=False
    # while loop
    while index+new_index < len(word_list)-1:
        # find first "the"
        if word_list[index]==word:
            # incrementing new_index by 1
            new_index+=1
            # find "a" or "a" in any in any word
            if word_list[index+new_index]=='a' or 'a' in word_list[index+new_index]:
                # add count to total_count
                total_count+=count
                # chnage count as 0
                count = 0
                # set status as True
                status=True
            # find next "the" when the status is False
            if  word_list[index+new_index]==word and status==False:
                # incrementing count by 1
                count+=1
                # change index to index + new_index
                index+=new_index
                # change new_index as 0
                new_index=0
            # find next "the" when the status is True
            if word_list[index+new_index]==word and status==True:
                # change index to index + new_index
                index+=new_index
                # set status as False
                status=False
    # add count to total_count
    total_count+=count
    # print total_count
    return total_count

# call the countWord()
count = countWord(word_list,'the')
# call the wordCount()
# count = wordCount(word_list,'the')
print("Count of 'the' followed by another 'the' is : ",count)