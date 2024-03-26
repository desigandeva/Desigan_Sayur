# build a calculator program
# 
# 3 * 5 -> 15
# 2 + 5 * 10 / 7 - 5 -> 5
# 
# (2+(5*2)/5-2) -> 2
# 
# 
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
def solveOpperators(input_list,opperator):
    # print('\n',input_list)
    # initialize empty list
    new_list = []
    # initialize index as 0
    index = 0
    # check the given opperator not pressent in the given input_list
    if input_list.count(opperator)==0:
        # return input_list
        return input_list
    else:
        # check index is less than lenngth of input_list
        while index < len(input_list):
            # find the opperator index in input list
            if input_list[index]==opperator:
                # remove the last added item in new_list stored into num1
                num1 = int(new_list.pop())
                # get the next item in input_list stored into num2
                num2 = int(input_list[index+1])
                # call the calculate() get the value and stored in new_list
                new_list.append(calculate(num1,opperator,num2))
                # incremect the ibdex by 1
                index+=1
            else:
                # add item into new_list
                new_list.append(input_list[index])
            # incremect the ibdex by 1
            index+=1
        # return call the solveOpperators() pass the new_list and opperator
        return solveOpperators(new_list,opperator)

# build the function solvebrackets()
def solveBrackets(input_list,bracket):
    # print('\n',input_list)
    # initialize empty list
    new_list = []
    # initialize index as 0
    index = 0
    # initialize result as 0
    result = 0
    # check given bracket is not present in input_list
    if input_list.count(bracket)==0:
        # return input_list
        return input_list
    else:
        # check index is lessthan length of input_list
        while index < len(input_list):
            # check the bracket index
            if input_list[index]==bracket:
                # remove the last added item and stored in num1
                num1 = int(new_list.pop())
                # remove the last added item and stored in opp
                opp = new_list.pop()
                # remove the last added item and stored in num2
                num2 = int(new_list.pop())
                # call calculate() get the value and stored into result
                result = calculate(num2,opp,num1)
                # remove the last added item
                new_list.pop()
                # add result into new_list
                new_list.append(result)
            else:
                # add item into new_list
                new_list.append(input_list[index])
            # increment index by 1
            index+=1
        # return solveBrackets() pass new_list and bracket
        return solveBrackets(new_list,bracket)

# build a function advance calculator
def advanceCalc(input_list):
    # orderOpperation = ['**','*','/','//','%','+','-']
    # call solveBracket() pass input_list and ')' store into new_list
    new_list = solveBrackets(input_list,')')
    # call solveOpperatoes() pass new_list and '**' store into new_list1
    new_list1 = solveOpperators(new_list,'**')
    # call solveOpperatoes() pass new_list1 and '*' store into new_list2
    new_list2 = solveOpperators(new_list1,'*')
    # call solveOpperatoes() pass new_list2 and '/' store into new_list3
    new_list3 = solveOpperators(new_list2,'/')
    # call solveOpperatoes() pass new_list3 and '//' store into new_list4
    # new_list4 = solveOpperators(new_list3,'//')
    # call solveOpperatoes() pass new_list4 and '%' store into new_list5
    # new_list5 = solveOpperators(new_list4,'%')
    # call solveOpperatoes() pass new_list3 and '+' store into new_list6
    new_list6 = solveOpperators(new_list3,'+')
    # call solveOpperatoes() pass new_list6 and '-' store into new_list7
    new_list7 = solveOpperators(new_list6,'-')
    # return new_list7
    return new_list7[0]




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

# build main() function
def main():
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
                print("Result : ",advanceCalc(input_list))
            else:
                # print invalid expression
                print("Enter valid expresstion")
    # execute any error will occure
    except Exception as e:
        # print error
        print(e)        

# call main()
main()