# get the input string from user
# print the string in pyramid 

# build function for pyramid
def pyramidPrint(string):
    for index in range(lengthOfString(string)):
        print(string[:index+1])

# build a function for find string length
def lengthOfString(string):
    length = 0
    for element in string:
        length += 1
    return length

# get input from user
pyramidPrint(input("Enter a input : "))