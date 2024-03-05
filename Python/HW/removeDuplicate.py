# get string input from user
# remove the duplicates in given input string

# build a function for removing duplicates
# def removeDuplicates(string):
#     newString = ''
#     for index in range(lengthOfString(string)-1):
#         if( string[index] != string[index+1] ):
#             newString = newString + string[index]
#     newString=newString+string[lengthOfString(string)-1]
#     return newString

def removeDuplicates(string):
    newString = ''
    for element in string:
        if element not in newString:
            newString+=element
    return newString

# build a function for length fo the string
# def lengthOfString(string):
#     length = 0
#     for index in string:
#         length += 1
#     return length

# def removeDuplicates():
#     dup = input("Enter any String :")
#     res = set()
#     #dup = hello
#     for i in dup : # It executes length of dup times
#         if i in res : # It executes 1 time
#             continue 
#         else : 
#             res.add(i)
#     print(res)

def removeDuplicate(para):
    newpara = ''
    for word in para:
        newWord = ''
        for character in word:
            if character not in newWord:
                newWord += character
        # print(newWord)
        newpara = newpara + newWord + ' '
    return newpara


para = removeDuplicate(input("enter input : ").split())
print(para)

# call the remove duplicate function and store new string
# newString = removeDuplicates(input("Enter a input : "))
# print(newString)
# removeDuplicates()