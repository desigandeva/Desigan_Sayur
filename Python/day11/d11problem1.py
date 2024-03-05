# get input string from user
# check the given ip is valid or not

# get input
ip_address = input("Enter a ip address : ")
# split the string
ip_address = ip_address.split('.')

# build function for check vaild ip
def validIp():
    if(len(ip_address)==4 and 0<=int(ip_address[0])<256 and
       0<=int(ip_address[1])<256 and 0<=int(ip_address[2])<256
       and 0<=int(ip_address[3])<256):
        return 1
    return 0

# validIp() return true it's vaild
if validIp():
    print("Valid Ip address")
# else not valid
else:
    print("Not a valid Ip address")