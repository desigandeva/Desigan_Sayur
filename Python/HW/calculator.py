# build a calculator program
# 
# 3 * 5 -> 15
# 2 + 5 * 10 / 7 - 5 -> 5
# 
# (2+(5*2)/5-2) -> 2
# 
# ((5+15*5)/(6+4)-(1+(5/5))) -> 6
# 

# build calulate function
def calculate(num1,opperator,num2):
    # check opperator is '+'
    if opperator=='+':
        # add num1 and num2 then return
        return num1+num2
    # check opperator is '-'
    if opperator=='-':
        # sub num1 and num2 then return
        return num1-num2
    # check opperator is '*'
    if opperator=='*':
        # mul num1 and num2 then return
        return num1*num2
    # check opperator is '/'
    if opperator=='/':
        # div num1 and num2 then return
        return num1/num2
    # check opperator is '//'
    if opperator=='//':
        # floor div num1 and num2 then return
        return num1//num2
    # check opperator is '%'
    if opperator=='%':
        # mod num1 and num2 then return
        return num1%num2
    # check opperator is '**'
    if opperator=='**':
        # pow num1 and num2 then return
        return num1**num2

# build solve opperatoes function
def solvePower(input_list):
    print('\n',input_list)
    # initialize empty list
    new_list = []
    # initialize index as 0
    index = 0
    # check the given opperator not pressent in the given input_list
    if input_list.count('**')==0:
        # return input_list
        return solveMulAndDiv(input_list)
    else:
        # check index is less than lenngth of input_list
        while index < len(input_list):
            # find the opperator index in input list
            if input_list[index]=='**':
                # remove the last added item in new_list stored into num1
                num1 = int(new_list.pop())
                # get the next item in input_list stored into num2
                num2 = int(input_list[index+1])
                # call the calculate() get the value and stored in new_list
                new_list.append(calculate(num1,'**',num2))
                # incremect the ibdex by 1
                index+=1
            else:
                # add item into new_list
                new_list.append(input_list[index])
            # incremect the ibdex by 1
            index+=1
        # return call the solveOpperators() pass the new_list and opperator
        return solvePower(new_list)

# build solve opperatoes function
def solveMulAndDiv(input_list):
    print('\n',input_list)
    # initialize empty list
    new_list = []
    # initialize index as 0
    index = 0
    # check the given opperator not pressent in the given input_list
    if input_list.count('*')==0 and input_list.count('/')==0:
        # return input_list
        return solveAddAndSub(input_list)
    else:
        # check index is less than lenngth of input_list
        while index < len(input_list):
            # find the opperator index in input list
            if input_list[index]=='*' or input_list[index]=='/':
                # remove the last added item in new_list stored into num1
                num1 = int(new_list.pop())
                # get the next item in input_list stored into num2
                num2 = int(input_list[index+1])
                # call the calculate() get the value and stored in new_list
                new_list.append(calculate(num1,input_list[index],num2))
                # incremect the ibdex by 1
                index+=1
            else:
                # add item into new_list
                new_list.append(input_list[index])
            # incremect the ibdex by 1
            index+=1
        # return call the solveOpperators() pass the new_list and opperator
        return solveMulAndDiv(new_list)

# build solve opperatoes function
def solveAddAndSub(input_list):
    print('\n',input_list)
    # initialize empty list
    new_list = []
    # initialize index as 0
    index = 0
    # check the given opperator not pressent in the given input_list
    if input_list.count('+')==0 and input_list.count('-')==0:
        # return input_list
        return input_list
    else:
        # check index is less than lenngth of input_list
        while index < len(input_list):
            # find the opperator index in input list
            if input_list[index]=='+' or input_list[index]=='-':
                # remove the last added item in new_list stored into num1
                num1 = int(new_list.pop())
                # get the next item in input_list stored into num2
                num2 = int(input_list[index+1])
                # call the calculate() get the value and stored in new_list
                new_list.append(calculate(num1,input_list[index],num2))
                # incremect the ibdex by 1
                index+=1
            else:
                # add item into new_list
                new_list.append(input_list[index])
            # incremect the ibdex by 1
            index+=1
        # return call the solveOpperators() pass the new_list and opperator
        return solveAddAndSub(new_list)

# build the function for finding last occurance of character
def findIndex(input_list,find_char):
    # revers the input_list and stored into new_list
    new_list = input_list[::-1]
    # for loop
    for index in range(len(new_list)):
        # find the character
        if new_list[index]==find_char:
            # return index possesion of given character in input_list
            return (len(new_list)-index-1)


# build the function solvebrackets()
def solveBrackets(input_list):
    print('\n',input_list)
    # initialize empty list
    new_list = []
    # initialize index as 0
    index = 0
    # initialize result as 0
    result = 0
    # check given bracket is not present in input_list
    if input_list.count(')')==0:
        # return input_list
        return solvePower(input_list)
    else:
        # check index is lessthan length of input_list
        while index < len(input_list):
            # check the bracket index
            if input_list[index]==')':
                # find the index of nearest oppen bracket
                start_index = findIndex(new_list,'(')
                # add the element in temp_list
                temp_list = new_list[start_index+1:]
                # remove the solved item in new_list
                for iterator in range(start_index,len(new_list)):
                    # remove the last added item
                    new_list.pop()
                # solve the temp_list call solvePower()
                result = solvePower(temp_list)
                # add result into new_list
                new_list.append(result[0])
            else:
                # add item into new_list
                new_list.append(input_list[index])
            # increment index by 1
            index+=1
        # return solveBrackets() pass new_list and bracket
        return solveBrackets(new_list)

# build the checkbal() to check the balance of '(',')','[',']','{','}'
def checkPerfectExpression(input_string):
    # initialize empty stack/list 
    stack = []
    try:
        # check every element is balsed or not
        for char in input_string:
                # chech the open parenthesis
                if char=="(":
                    # add the char to stack/list
                    stack.append(char)
                # chech the close parenthesis
                elif char==")":
                    # remove the char from stack/list
                    stack.pop()
                # chech the open curly bracket
                if char=="{":
                    # add the char to stack/list
                    stack.append(char)
                # chech the close curly bracket
                elif char=="}":
                    # remove the char from stack/list
                    stack.pop()
                # chech the open square bracket
                if char=="[":
                    # add the char to stack/list
                    stack.append(char)
                # chech the close square bracket
                elif char=="]":
                    # remove the char from stack/list
                    stack.pop()
        # return true
        return True
    # any error will occure
    except Exception as e:
        print(e)
        # return false
        return False

# build a function advance calculator
def advancedCalc():
    # execute try block
    try:
        # infinite loop
        while True:
            # get the expression from user
            input_string = input("Enter your equation (seperate by space) : ")
            # chcek the given expression is perfect
            if checkPerfectExpression(input_string):
                # change string into list
                input_list = input_string.split()
                # call the advanceCalc() pass input_list
                print("Result : ",solveBrackets(input_list)[0])
            else:
                # print invalid expression
                print("Enter valid expresstion")
    # execute any error will occure
    except Exception as e:
        # print error
        print(e)        

# call advancedCalc()
advancedCalc()
