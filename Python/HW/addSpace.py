# get input string from user
# add space in input string for each and every 3rd element

# build a function for adding space for each 3rd element
def addSpace(string):
    index = 0
    count = 1
    newString = ''
    while index < lengthOfString(string):
        if(count==3):
            newString = newString + " "
            count = 1
        newString = newString + string[index]
        count += 1
        index += 1
    return newString

# build a function for find length of string
def lengthOfString(string):
    length = 0
    for element in string:
        length += 1
    return length

# call the addSpace() function to add the space and print new string
print(addSpace(input("Enter a input : ")))