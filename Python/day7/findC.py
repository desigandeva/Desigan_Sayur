# Problem 3:
#   In the input, find the first A and last A, print all the letters between these two A. 
#   If there is no A or 2nd A is not found, find the first B after the first A (if there is a A) and last B and print all the letters between these two B.   
#   If there is no B or 2nd B is not found, find the first C after the first B (if there is a B) and last C and print all the letters between these two C. 
# 
# read a passage from the 'file1.txt' and change to lower case
# find first 'a' and last 'a' if 2nd a is not there find first amd last 'b' after first 'a'
# if 2nd 'b' is not there find first and last 'c' after first 'b
# using find() and rfind(), this are inbuild functions
# 

# open file and store to passage
input_file = open("./Python/day7/file2.txt","r")
# read file and change to lower case
passage = input_file.read().lower()
# set array to store the find letter
arr = ['a','b','c']

# build the function to find the letters in between
def findLetter(passage,n):
    # find the first letter index
    first_letter_index = passage.find(arr[n])
    # find last letter index
    last_letter_index = passage.rfind(arr[n])
    # check if 2nd letter is missing find next letter
    if(first_letter_index==last_letter_index):
        # also change the passage from the first letter
        passage = passage[first_letter_index:]
        print("2nd",arr[n],"is not there.")
        # find the next letter
        findLetter(passage,n+1)
    # if 2nd letter is there print the in between letters 
    else:
        print("Between first and last ",arr[n]," is,\n\n",passage[first_letter_index:last_letter_index+1],sep='')


# call the findLetter() function
findLetter(passage,0)