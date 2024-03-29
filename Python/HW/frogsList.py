# There are frogs walking in a line represented in the form of a list.
# The numbers in the list are the size of frogs. A frog(at position i) will eat the previous frog (i-1),
# if the previous frog is smaller in size. Print the alive frogs in the list 
# Input : [1,2,5,4,3,2,2]
# Output : [5,4,3,2,2]
# Explanation : Frog (1) ate Frog(0); Frog(2) ate Frog (1). Rest of the frogs are alive
# Input : [4,3,3,2,1]
# Output : [4,3,3,2,1]
# 
# Imagine the frog becomes bigger as much as the size of the frog it ate. How would it change the program
# 
# 
# 

# build a function for find alive frog's
def findAliveFrogs(frog_list):
    # assign alive_frog_list as first frog size in frog_list
    alive_frog_list = [0]
    # get all frog's from frog_list one by one
    for index in range(len(frog_list)):
        # check the current frog size is graterthan the last frog size in alive_frog_list
        if alive_frog_list[-1] >= frog_list[index]:
            # add the frogin alive_frog_list
            alive_frog_list.append(frog_list[index])
        # else
        else:
            # remove the frog from alive_frog_list
            size = alive_frog_list.pop()
            # add the current frog in alive_frog_list with added added size of removed frog size
            alive_frog_list.append(frog_list[index]+size)
    # return alive_frog_list
    return alive_frog_list

# get input grof size from user seperated by , and spit into list
# map the value to input_list in int datatype
input_list = list(map(int,input("Enter frog size (seperate by ,) : ").split(',')))
# print the alive frog list
print("Alive Frog List is : ",findAliveFrogs(input_list))