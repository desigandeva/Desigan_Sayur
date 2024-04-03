# Problem #5
# Same as above, but the operator come first.
# eg - input ["+","1", "2", "*", "5"]
# output =  15
# explanation (1 + 2) * 5 = 15
# input ["-","10", "+", "2", "3", "*", "5"]
# output =  25
# explanation (10 - ( 2 + 3)) * 5 = 25
# 
# get list
# find operator do those opperation
# after push into list
# 

# list1
mlist = ["+","1", "2", "*", "5"]
# mlist = ["-","10", "+", "2", "3", "*", "5"]

# build a function for solve the equation
def solveEquation(list1):
    # empty list
    result = []
    # init index is 0
    index = 0
    # check length of list is <= 3
    if len(list1)<=3:
        # add
        if list1[1]=='+':
            return int(list1[0])+int(list1[2])
        # mul
        elif list1[1]=='*':
            return int(list1[0])*int(list1[2])
        # sub
        elif list1[1]=='-':
            return int(list1[0])-int(list1[2])
        # div
        elif list1[1]=='/':
            return int(list1[0])/int(list1[2])
    # lenght of list is more than 3
    else:
        while index < len(list1):
            # index is digit append to new list
            if list1[index].isdigit():
                result.append(list1[index])
            # add
            elif(list1[index]=='+' and index<len(list1)-2 and list1[index+2].isdigit() ):
                result.append(str(int(list1[index+1])+int(list1[index+2])))
                index+=2
            # sub
            elif(list1[index]=='-' and index<len(list1)-2 and list1[index+2].isdigit() ):
                result.append(str(int(list1[index+1])-int(list1[index+2])))
                index+=2
            # mul
            elif(list1[index]=='*' and index<len(list1)-2 and list1[index+2].isdigit() ):
                result.append(str(int(list1[index+1])*int(list1[index+2])))
                index+=2
            # div
            elif(list1[index]=='/' and index<len(list1)-2 and list1[index+2].isdigit() ):
                result.append(str(int(list1[index+1])/int(list1[index+2])))
                index+=2
            # add to new list
            else:
                result.append(list1[index])
            index+=1
        # print(result)
        # return list 
        return solveEquation(result)

# call solveequation() function
print(solveEquation(mlist))