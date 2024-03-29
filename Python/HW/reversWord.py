# Reverse a string: Given a string, reverse it using a stack.
# Eg : Hello -> olleH
# 
# Given string str, we need to print the reverse of individual words. (dont use built in functions)
# Input : Hello World
# Output : olleH dlroW
# 
# 

# build a function for revers the given string
def reversWordUseStack(input_string):
    # assign empty stack/list 
    stack = []
    # assign empty string
    output_string = ""
    # get each char one by one in loop
    for char in input_string:
        # add the char in stack
        stack.append(char)
    # iterate all value in stack
    for index in range(len(stack)):
        # revome the last char in stack is added to output_string
        output_string += stack.pop()
    # return the output_string
    return output_string

# build the function for revers the each word in string
def reversWordInString(input_string):
    # assign empty output_string
    output_string = ""
    # convert string into list
    word_list = input_string.split()
    # get word from word_list one by one
    for word in word_list:
        # revers the word and add the revers word in output_string
        output_string += word[::-1] + ' '
    # return output_string
    return output_string


# get input from user
input_string = input("Enter input : ")
# print the revers word
print("Revers word : ",reversWordUseStack(input_string))
# print revers word in string
print("Revers each word : ",reversWordInString(input_string))