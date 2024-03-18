# Problem 2:
#   In the input, find the first A and last A, print all the letters between these two A. 
#   If there is no A or 2nd A is not found, find the first B  and last B and print all the letters between these two B. 
#   If there is no B or 2nd B is not found, find the first C and last C and print all the letters between these two C. 
# 
# read a passage from the 'file1.txt' and change to lower case
# find first 'a' and last 'a' if 2nd a is not there find first amd last 'b'
# using find() and rfind(), this are inbuild functions
# 
# open file and store to txt_file
txt_file = open("./Python/day7/file1.txt","r")
# read file and change to lower case
passage = txt_file.read().lower()
# find this values
arr = ['a','b']

def findLetter(n):
    letter = arr[n]
    # find first letter
    first_letter_index = passage.find(letter)
    # find last letter
    last_letter_index = passage.rfind(letter)
    # return first_letter,last_letter
    if(first_letter_index==last_letter_index):
        print("2nd",arr[n],"is not there")
        findLetter(n+1)
    else:
        print(passage[first_letter_index:last_letter_index+1])

# call the findLetter() function
findLetter(0)