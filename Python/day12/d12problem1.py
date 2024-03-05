# You have list of unique words. you input is a string with no spaces.
# Return true if the letters in the 
# input string can be seperated into words that are in the list.
# eg list = ["we", "students", "are" ]

# my list
my_list = ["we","students","are"]
# get input passage
passage = input()
# build function for check word
def checkWord(passage,my_list):
    for i in my_list:
        if i in passage:
            passage=passage.replace(i,'')
    if(len(passage)==0):
        return True
    else:
        return False

# print the results
print(checkWord(passage,my_list))