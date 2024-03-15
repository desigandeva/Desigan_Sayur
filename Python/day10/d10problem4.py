# get the list 
# Convert to integer, push it to a stack
# operator occure pop two elements from the stack
# apply the operation and push the result back


list1 = ['10','2','3','+','-','5','*']
# list1 = ['1','2','+','5','*']
result = []
for i in list1:
    # '+' occur pop 2 element and add those num and push 
    if(i=='+'):
        s1 = result.pop()
        s2 = result.pop()
        result.append(s1+s2)
    # '-' occur pop 2 element and sub those num and push 
    elif(i=='-'):
        s1 = result.pop()
        s2 = result.pop()
        result.append(s2-s1)
    # '*' occur pop 2 element and mul those num and push 
    elif(i=='*'):
        s1 = result.pop()
        s2 = result.pop()
        result.append(s1*s2)
    # '/' occur pop 2 element and div those num and push 
    elif(i=='/'):
        s1 = result.pop()
        s2 = result.pop()
        result.append(s1/s2)
    # numbers occure push to list
    else:
        result.append(int(i))

# print result
print(result[0])