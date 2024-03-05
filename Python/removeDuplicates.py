# get string input from user
# remove the duplicates in given input string


def removeDuplicates(string):
    newString = ''
    for element in string:
        if element not in newString:
            newString+=element
    return newString

def removeDuplicate(para):
    newpara = ''
    for word in para:
        newWord = ''
        for character in word:
            if character not in newWord:
                newWord += character
        newpara = newpara + newWord + ' '
    return newpara

# call the remove duplicate function and store new string
inputString = input("enter input : ")
inputString1 = inputString.lower().split()
inputString2 = inputString.split()
para1 = removeDuplicate(inputString1)
print("Without case : "+para1)
para2 = removeDuplicate(inputString2)
print("With case :"+para2)