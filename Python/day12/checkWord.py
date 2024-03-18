# Problem #1
# You have list of unique words. you input is a string with no spaces. Return true if the letters in the 
# input string can be seperated into words that are in the list.
# eg list = ["we", "students", "are" ]
# input = "wearestudents"
# output = true
# eg 2 List = ["we", "doctor","and", "nurse", "are"]
# input = "wearenurseandoctor"
# output = False 
# input = "wearenurseanddoctor"
# output = true
# 
# You have list of unique words. you input is a string with no spaces.
# Return true if the letters in the 
# input string can be seperated into words that are in the list.
# eg list = ["we", "students", "are" ]
# 

# my list
my_list = ["we","students","are"]
# get input passage
passage = input()
# build function for check word
def checkWord(passage,my_list):
    for word in my_list:
        # check the word in passage
        if word in passage:
            # remove the word in passage
            passage=passage.replace(word,'')
    # length of passage is 0 return True
    if(len(passage)==0):
        return True
    # else return False
    else:
        return False

# print the results
print(checkWord(passage,my_list))