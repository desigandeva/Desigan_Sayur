# get user input to print how many rows and stored in 'n'
n=input("Enter no of rows : ")
# assign empty string as 's
s=""

for i in range(1,int(n)+1):
    if i==1:
        s=str(i)
    else:
        s=str(i)+s+str(i)
    print(s)