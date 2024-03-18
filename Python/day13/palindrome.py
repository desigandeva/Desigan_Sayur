# Problem #1
# Input is a range of numbers as string. Print only the numbers that are palindromes and also the 
# square of that number is also a palindrome.
# eg. 121 is a palindrome and 121 * 121 = 14641 is also a palindrome, so you can print 121
# 131 is a palindrome, but 131*131 = 17161 is not a palindrome,so you can't print it.
# eg input "10", "500"
# Make sure to identify which steps need to be a function, how to avoid unnecessary parsing 
# of numbers. Checking for palidrome or not, should be an efficient code.
# 
# get input is a range of numbers as string
# check number is palidrome and also square of same is also a palidrome
# 

# get input 
input_num_list = input("Enrter numbers (seperate by ,) : ").split(',')
# assign initial value
input_num1 = int(input_num_list[0])
# assign last value
input_num2 = int(input_num_list[1])

# build the function for check number is palindrome or not
def checkPalindrome(num):
    # change int to string
    num = str(num)
    # check rever order same as orginal order
    if(num==num[::-1]):
        # return 1
        return 1
    # else return 0
    return 0

for iterator in range(input_num1,input_num2):
    if checkPalindrome(iterator):
        if checkPalindrome(iterator*iterator):
            # print palindrome
            print(iterator,"is an palindrome")