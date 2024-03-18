# Problem #1
# 1. Check whether the given string input is a valid ip address.
# Find out what are the constraints for an ip address (how many chars, what numbers are allowed, how many '.' etc)
# Write all constraints.
# Get an input as string. Return if it is valid or not. 
# Use string functions.
# 
# get input string from user
# check the given ip is valid or not

# get input
ip_address = input("Enter a ip address : ")
# split the string
ip_address_list = ip_address.split('.')

# build function for check vaild ip
def validIp(ip_address_list):
    # check length of ip_address_list is 4
    # each item in the range(0<255)
    if(len(ip_address_list)==4 and 0<=int(ip_address_list[0])<256 and
       0<=int(ip_address_list[1])<256 and 0<=int(ip_address_list[2])<256
       and 0<=int(ip_address_list[3])<256):
        # return 1
        return 1
    # return 0
    return 0

# validIp() return true it's vaild
if validIp(ip_address_list):
    print("Valid Ip address")
# else not valid
else:
    print("Not a valid Ip address")