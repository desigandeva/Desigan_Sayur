# get input is a range of numbers as string
# check number is palidrome and also square of same is also a palidrome

# get input 
n = input("Enrter numbers (seperate by ,) : ").split(',')
# assign initial value
n1 = int(n[0])
# assign last value
n2 = int(n[1])

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

for i in range(n1,n2):
    if checkPalindrome(i):
        if checkPalindrome(i*i):
            # print palindrome
            print(i,"is an palindrome")