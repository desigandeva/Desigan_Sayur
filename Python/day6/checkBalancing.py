# Program #1
# Write a program to check if a given string of parentheses, brackets, and braces is balanced. 
# For instance, "({[]})" is balanced, but "({[)})" is not
# Input - (Abc[i]) or (Abc[2])
# Output true
# Input ((Abc[i]) or (Abc[2])) 
# Output true
# Input ((Abc[i]) or Abc[2)])
# Output False
# 
# check if a given string of parentheses, brackets, and braces is balanced. 
# For instance, "({[]})" is balanced, but "({[)})" is not
# 
# assign '(' -> 1 and ')' -> -1
# '[' -> 2 and ']' -> -2
# '{' -> 3 and '}' -> -3
# 

# assume the string is stored in 'a'
input_string = "((Abc[i]) or (Ab[2]))"

# build the checkbal() to check the balance of '(',')','[',']','{','}'
def checkBal(input_string):
    # assign initial as 0
    count = 0
    # check every element is balsed or not
    for character in input_string:
        if character=='(':
            # add count by 1
            count+=1
        elif character==')':
            # sub count by 1
            count-=1
        elif character=='[':
            # add count by 2
            count+=2
        elif character==']':
            # sub count by 2
            count-=2
        elif character=='{':
            # add count by 3
            count+=3
        elif character=='}':
            # sub count by 3
            count-=3
    # if count is 0 then return true (it's balansed)
    if count==0:
        return True
    # if count not 0 then return false (it's unbalanced)
    else:
        return False

# print and call the checkBal() function
print(checkBal(input_string))