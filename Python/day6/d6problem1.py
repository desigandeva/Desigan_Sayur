# check if a given string of parentheses, brackets, and braces is balanced. 
# For instance, "({[]})" is balanced, but "({[)})" is not
# 
# assign '(' -> 1 and ')' -> -1
# '[' -> 2 and ']' -> -2
# '{' -> 3 and '}' -> -3
# assume the string is stored in 'a'
a = "((Abc[i]) or (Ab[2]))"

# build the checkbal() to check the balance of '(',')','[',']','{','}'
def checkBal(string):
    # assign initial as 0
    c = 0
    # check every element is balsed or not
    for i in string:
        if i=='(':
            c+=1
        elif i==')':
            c-=1
        elif i=='[':
            c+=2
        elif i==']':
            c-=2
        elif i=='{':
            c+=3
        elif i=='}':
            c-=3
    # if c is 0 then return true (it's balansed)
    if c==0:
        return True
    # if c not 0 then return false (it's unbalanced)
    else:
        return False

# print and call the checkBal() function
print(checkBal(a))