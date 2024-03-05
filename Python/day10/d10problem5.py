# get list
# find operator do those opperation
# after push into list

# list1
mlist = ["+","1", "2", "*", "5"]
# mlist = ["-","10", "+", "2", "3", "*", "5"]

# build a function for solve the equation
def solveEquation(list1):
    # empty list
    result = []
    # init i is 0
    i = 0
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
        while i < len(list1):
            # i is digit append to new list
            if list1[i].isdigit():
                result.append(list1[i])
            # add
            elif(list1[i]=='+' and i<len(list1)-2 and list1[i+2].isdigit() ):
                result.append(str(int(list1[i+1])+int(list1[i+2])))
                i+=2
            # sub
            elif(list1[i]=='-' and i<len(list1)-2 and list1[i+2].isdigit() ):
                result.append(str(int(list1[i+1])-int(list1[i+2])))
                i+=2
            # mul
            elif(list1[i]=='*' and i<len(list1)-2 and list1[i+2].isdigit() ):
                result.append(str(int(list1[i+1])*int(list1[i+2])))
                i+=2
            # div
            elif(list1[i]=='/' and i<len(list1)-2 and list1[i+2].isdigit() ):
                result.append(str(int(list1[i+1])/int(list1[i+2])))
                i+=2
            # add to new list
            else:
                result.append(list1[i])
            i+=1
        # print(result)
        # return list 
        return solveEquation(result)

# call solveequation() function
print(solveEquation(mlist))