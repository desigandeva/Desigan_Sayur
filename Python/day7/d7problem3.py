# read a passage from the 'file1.txt' and change to lower case
# find first 'a' and last 'a' if 2nd a is not there find first amd last 'b' after first 'a'
# if 2nd 'b' is not there find first and last 'c' after first 'b
# using find() and rfind(), this are inbuild functions
# 
# open file and store to passage
passage = open("./day7/file2.txt","r")
# read file and change to lower case
passage = passage.read().lower()
# set array to store the find letter
arr = ['a','b','c']

# build the function to find the letters in between
def findLetter(passage,n):
    first_letter = passage.find(arr[n])
    last_letter = passage.rfind(arr[n])
    # check if 2nd letter is missing find next letter
    if(first_letter==last_letter):
        # also change the passage from the first letter
        passage = passage[first_letter:]
        print("2nd",arr[n],"is not there.")
        # find the next letter
        findLetter(passage,n+1)
    # if 2nd letter is there print the in between letters 
    else:
        print("Between first and last ",arr[n]," is,\n\n",passage[first_letter:last_letter+1],sep='')


# call the findLetter() function
findLetter(passage,0)