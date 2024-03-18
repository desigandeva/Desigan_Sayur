# problem #4
# write a program to find if two strings are same.
# two string are considered same if both strings have same letters in same order, but from different starting point
# eg abcd is same as bcda (a is moved to the right)
# abcd is same as cdab 
# abcd is  not same as cdba
# 
# 123456 = 456123
# 123456 not = 412356
# hint - 
# there are many simple answers. you can try with slice function
# 
# get two strings from user
# check weather the strings are same letters and order but in different string point
# slice() on of the in-build function it's used to slice the string
# 

# get 1st input and store in 'str1'
str1 = input("Enter a 1st string : ")
# get 2nd input and store in 'str2'
str2 = input("Enter a 2nd string : ")

# build a function to check the characters
def checkLetter():
    for character in range(0,len(str1)):
        # print(str1[character:]+str1[slice(character)])
        if(str2==(str1[character:]+str1[slice(character)])):
            # return 1
            return 1

# call the checkLetter() method
if checkLetter():
    # print the strings are same chrater and order but diffenter string piont
    print("Given strings are same")
else:
    # else print not same
    print("Given string are not same")