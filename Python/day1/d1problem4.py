# get two strings from user
# check weather the strings are same letters and order but in different string point
# slice() on of the in-build function it's used to slice the string

# get 1st input and store in 'str1'
str1 = input("Enter a 1st string : ")
# get 2nd input and store in 'str2'
str2 = input("Enter a 2nd string : ")

def checkLetter():
    for i in range(0,len(str1)):
        # print(str1[i:]+str1[slice(i)])
        if(str2==(str1[i:]+str1[slice(i)])):
            return 1
if checkLetter():
    # print the strings are same chrater and order but diffenter string piont
    print("Given strings are same")
else:
    print("Given string are not same")