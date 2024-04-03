# factorial
# 5! -> 5*4*3*2*1

# build factorial function
def factorial(num):
    # check base condition
    if num==1:
        # return num
        return num
    # else
    else:
        # call factoial() in decrement num by 1
        # mul with num then return
        return num * factorial(num-1)
    
# get user input
input_num = int(input("Enter the number : "))
# fild factorial of given input number
result = factorial(input_num)
# print result
print(input_num,"! is : ",result,sep='')