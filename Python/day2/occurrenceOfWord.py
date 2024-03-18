# Problem #2
# Write a program that reads a passage or string and counts the occurrences of two consecutive words 
# that are the same without any other specific word in between.
#  For example, count the occurrences of "apple apple" but not "apple orange apple."
# 
# read a passage or string and counts the occurrences of two consecutive words 
# that are the same without any other specific word in between.
# 

# get user string and stored in 'passage'
word_list = input("Enter the passage : ").split()
# assign count as 1 default
count=1

# check all word in the word_list
for index in range(0,len(word_list)):
    if(index<len(word_list)-1):
        # find occurrences of two consecutive words
        if(word_list[index]==word_list[index+1]):
            # increment the count value
            count+=1

# print the count
print(count)