# Problem #4
# Input is an array of strings of an arithmetic expression. Calculate the value.
# eg - input ["1", "2", "+", "5", "*"]
# output =  15
# explanation (1 + 2) * 5 = 15
# 
# input ["10", "2", "3", "+","-", "5", "*"]
# output =  25
# explanation (10 - ( 2 + 3)) * 5 = 25
# Hint : Use the concept of stack. Push and pop. 
# Parse the input list one element at a time. Convert to integer, push it to a stack. Whenever you see an
# operator, pop two elements from the stack, apply the operation and push the result back.
# 
# get the list 
# Convert to integer, push it to a stack
# operator occure pop two elements from the stack
# apply the operation and push the result back
# 

list1 = ['10','2','3','+','-','5','*']
# list1 = ['1','2','+','5','*']
result = []
for item in list1:
    # '+' occur pop 2 element and add those num and push 
    if(item=='+'):
        val1 = result.pop()
        val2 = result.pop()
        result.append(val1+val2)
    # '-' occur pop 2 element and sub those num and push 
    elif(item=='-'):
        val1 = result.pop()
        val2 = result.pop()
        result.append(val2-val1)
    # '*' occur pop 2 element and mul those num and push 
    elif(item=='*'):
        val1 = result.pop()
        val2 = result.pop()
        result.append(val1*val2)
    # '/' occur pop 2 element and div those num and push 
    elif(item=='/'):
        val1 = result.pop()
        val2 = result.pop()
        result.append(val1/val2)
    # numbers occure push to list
    else:
        result.append(int(item))

# print result
print(result[0])