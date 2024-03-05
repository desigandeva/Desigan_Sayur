# read a passage or string and counts the occurrences of two consecutive words 
# that are the same without any other specific word in between.

# get user string and stored in 'passage'
passage = input("Enter the passage : ").split()
# assign count as 1 default
count=1

# check all word in the passage
for i in range(0,len(passage)):
    if(i<len(passage)-1):
        # find two consecutive words
        if(passage[i]==passage[i+1]):
            # increment the count value
            count+=1

# print the count
print(count)