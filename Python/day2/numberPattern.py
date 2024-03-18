# Problem #1
# Print the following pattern
# 1
# 212
# 32123
# 4321234
# 543212345
# Get user input for how far to go (up to 0)
# 

# get user input and stored in 'rows'
rows=input("Enter no of rows : ")
# assign empty string as 'tmp_string'
tmp_string=""

for num in range(1,int(rows)+1):
    if num==1:
        # store the num in tmp_string
        tmp_string=str(num)
    else:
        # store the num+tmp_string+num in tmp_string 
        tmp_string=str(num)+tmp_string+str(num)
    # print the tmp_string
    print(tmp_string)