# 3. Same as above, but the input is given without any . 
# Print all possible ipaddress based on the contraints learnt in problem 1.
# eg input - 0000
# output 0.0.0.0
# input 10026710
# output 100.2.67.10
# input 100242200
# output 100.24.220.0, 100.242.20.0
# 
# get string value from user input
# change the given string to valid ip address
# 

# build function for string to ip address
def stringToIP(string):
    length_of_str = len(string)
    # print(length_of_str)
    if(4<=length_of_str<=12):
        if(length_of_str==4):
            print(string[0]+'.'+string[1]+'.'+string[2]+'.'+string[3])
        elif(length_of_str==5):
            print(string[:2]+'.'+string[2]+'.'+string[3]+'.'+string[4])
            print(string[0]+'.'+string[1:3]+'.'+string[3]+'.'+string[4])
            print(string[0]+'.'+string[1]+'.'+string[2:4]+'.'+string[4])
            print(string[0]+'.'+string[1]+'.'+string[2]+'.'+string[3:])
        elif(length_of_str==6):
            if(0<=int(string[:3])<256):
                print(string[:3]+'.'+string[3]+'.'+string[4]+'.'+string[5])
            if(0<=int(string[1:4])<256):
                print(string[0]+'.'+string[1:4]+'.'+string[4]+'.'+string[5])
            if(0<=int(string[2:5])<256):
                print(string[0]+'.'+string[1]+'.'+string[2:5]+'.'+string[5])
            if(0<=int(string[3:])<256):
                print(string[0]+'.'+string[1]+'.'+string[2]+'.'+string[3:])
            else:
                print(string[:2]+'.'+string[2:4]+'.'+string[4]+'.'+string[5])
                print(string[0]+'.'+string[1:3]+'.'+string[3:5]+'.'+string[5])
                print(string[0]+'.'+string[1]+'.'+string[2:4]+'.'+string[4:])
                print(string[:2]+'.'+string[2]+'.'+string[4]+'.'+string[4:])

        elif(length_of_str==7):
            if(0<=int(string[:3])<256):
                print(string[:3]+'.'+string[3:5]+'.'+string[5]+'.'+string[6])
                print(string[:3]+'.'+string[3]+'.'+string[4:6]+'.'+string[6])
                print(string[:3]+'.'+string[3]+'.'+string[4]+'.'+string[5:])
            if(0<=int(string[1:4])<256):
                print(string[:2]+'.'+string[2:5]+'.'+string[5]+'.'+string[6])
                print(string[0]+'.'+string[1:4]+'.'+string[4:6]+'.'+string[6])
                print(string[0]+'.'+string[1:4]+'.'+string[4]+'.'+string[5:])
            if(0<=int(string[2:5])<256):
                print(string[0]+'.'+string[1]+'.'+string[2:5]+'.'+string[5])
                print(string[:2]+'.'+string[2]+'.'+string[3:6]+'.'+string[6])
                print(string[0]+'.'+string[1]+'.'+string[2:5]+'.'+string[5:])
            if(0<=int(string[3:6])<256):
                print(string[0]+'.'+string[1:3]+'.'+string[3:6]+'.'+string[6])
                print(string[:2]+'.'+string[2]+'.'+string[3:6]+'.'+string[6])
            if(0<=int(string[4:])<256):
                print(string[0]+'.'+string[1]+'.'+string[2:4]+'.'+string[4:])
                print(string[0]+'.'+string[1:3]+'.'+string[3]+'.'+string[4:])
                print(string[:2]+'.'+string[2]+'.'+string[3]+'.'+string[4:])
            else:
                print(string[:2]+'.'+string[2:4]+'.'+string[4:6]+'.'+string[6])
                print(string[:2]+'.'+string[2:4]+'.'+string[4]+'.'+string[5:])
                print(string[:2]+'.'+string[2]+'.'+string[3:5]+'.'+string[5:])
                print(string[0]+'.'+string[1:3]+'.'+string[3:5]+'.'+string[5:])
        elif(length_of_str==8):
            if(0<=int(string[:3])<256):
                print(string[:3]+'.'+string[3:6]+'.'+string[6]+'.'+string[7])
                print(string[:3]+'.'+string[3]+'.'+string[4:7]+'.'+string[7])
                print(string[:3]+'.'+string[3]+'.'+string[4]+'.'+string[5:])
                print(string[:3]+'.'+string[3:5]+'.'+string[5:7]+'.'+string[7])
                print(string[:3]+'.'+string[3]+'.'+string[4:6]+'.'+string[6:])
                print(string[:3]+'.'+string[3:5]+'.'+string[5]+'.'+string[6:])
            if(0<=int(string[1:4])<256):
                print(string[:2]+'.'+string[2:5]+'.'+string[5:7]+'.'+string[7])
                print(string[0]+'.'+string[1:4]+'.'+string[4:6]+'.'+string[6:])
                print(string[:2]+'.'+string[2:5]+'.'+string[5]+'.'+string[6:])
                print(string[0]+'.'+string[1:4]+'.'+string[4]+'.'+string[5:])
                print(string[0]+'.'+string[1:4]+'.'+string[4:7]+'.'+string[7])
            if(0<=int(string[2:5])<256):
                print(string[:2]+'.'+string[2:4]+'.'+string[4:7]+'.'+string[7])
                print(string[:2]+'.'+string[2]+'.'+string[3:6]+'.'+string[6:])
                print(string[0]+'.'+string[1:3]+'.'+string[3:6]+'.'+string[6:])
                print(string[0]+'.'+string[1]+'.'+string[2:5]+'.'+string[5:])
            if(0<=int(string[3:])<256):
                print(string[:2]+'.'+string[2:4]+'.'+string[5]+'.'+string[5:])
                print(string[:2]+'.'+string[2]+'.'+string[3:5]+'.'+string[5:])
                print(string[0]+'.'+string[1:3]+'.'+string[3:5]+'.'+string[5:])
            else:
                print(string[:2]+'.'+string[2:4]+'.'+string[4:6]+'.'+string[6:])
                
        elif(length_of_str==9):
            if(0<=int(string[:3])<256 and 0<=int(string[3:6])<256): 
                print(string[:3]+'.'+string[3:6]+'.'+string[6:8]+'.'+string[8])
                print(string[:3]+'.'+string[3:6]+'.'+string[6]+'.'+string[7:])
            if(0<=int(string[:3])<256 and 0<=int(string[5:8])<256): 
                print(string[:3]+'.'+string[3:5]+'.'+string[5:8]+'.'+string[8])
            if(0<=int(string[:3])<256 and 0<=int(string[4:7])<256): 
                print(string[:3]+'.'+string[3]+'.'+string[4:7]+'.'+string[7:])
            if(0<=int(string[:3])<256 and 0<=int(string[6:])<256): 
                print(string[:3]+'.'+string[3:5]+'.'+string[5]+'.'+string[6:])
                print(string[:3]+'.'+string[3]+'.'+string[4:6]+'.'+string[6:])
            if(0<=int(string[2:5])<256 and 0<=int(string[5:8])):
                print(string[:2]+'.'+string[2:5]+'.'+string[5:8]+'.'+string[8])
            if(0<=int(string[1:4])<256 and 0<=int(string[4:7])):
                print(string[0]+'.'+string[1:4]+'.'+string[4:7]+'.'+string[7:])
            if(0<=int(string[1:4])<256 and 0<=int(string[6:])):
                print(string[0]+'.'+string[1:4]+'.'+string[4:6]+'.'+string[6:])
            if(0<=int(string[3:6])<256 and 0<=int(string[6:])):
                print(string[:2]+'.'+string[2]+'.'+string[3:6]+'.'+string[6:])
                print(string[0]+'.'+string[1:3]+'.'+string[3:6]+'.'+string[6:])

        elif(length_of_str==10):
            if(0<=int(string[:3])<256 and 0<=int(string[3:6])<265):
                print(string[:3]+'.'+string[3:6]+'.'+string[6:8]+'.'+string[8:])
            if(0<=int(string[5:8])<256 and 0<=int(string[:3])<256):
                print(string[:3]+'.'+string[3:5]+'.'+string[5:8]+'.'+string[8:])
            if(0<=int(string[:3])<256 and 0<=int(string[7:])<256):
                print(string[:3]+'.'+string[3:5]+'.'+string[5:7]+'.'+string[7:])
            if(0<=int(string[2:5])<256 and 0<=int(string[5:8])<256):
                print(string[:2]+'.'+string[2:5]+'.'+string[5:8]+'.'+string[8:])
            if(0<=int(string[4:7])<256 and 0<=int(string[7:])<256):
                print(string[:2]+'.'+string[2:4]+'.'+string[4:7]+'.'+string[7:])
            if(0<=int(string[2:5])<256 and 0<=int(string[7:])<256):
                print(string[:2]+'.'+string[2:5]+'.'+string[5:7]+'.'+string[7:])
            if(0<=int(string[1:4])<256 and 0<=int(string[4:7])<256 and 0<=int(string[7:])<256):
                print(string[0]+'.'+string[1:4]+'.'+string[4:7]+'.'+string[7:])
            if(0<=int(string[:3])<256 and 0<=int(string[4:7])<256 and 0<=int(string[7:])<256):
                print(string[:3]+'.'+string[3]+'.'+string[4:7]+'.'+string[7:])
            if(0<=int(string[:3])<256 and 0<=int(string[7:])<256 and 0<=int(string[3:6])<265):
                print(string[:3]+'.'+string[3:6]+'.'+string[6]+'.'+string[7:])
            if(0<=int(string[:3])<256 and 0<=int(string[3:6])<265 and 0<=int(string[6:9])<256):
                print(string[:3]+'.'+string[3:6]+'.'+string[6:9]+'.'+string[9])

        elif(length_of_str==11):
            if(0<=int(string[:3])<256 and 0<=int(string[3:6])<256 and 0<=int(string[6:9])<256):
                print(string[:3]+'.'+string[3:6]+'.'+string[6:9]+'.'+string[9:])
            if(0<=int(string[2:5])<256 and 0<=int(string[5:8])<256 and 0<=int(string[8:])<256):
                print(string[:2]+'.'+string[2:5]+'.'+string[5:8]+'.'+string[8:])
            if(0<=int(string[:3])<256 and 0<=int(string[5:8])<256 and 0<=int(string[8:])<256):
                print(string[:3]+'.'+string[3:5]+'.'+string[5:8]+'.'+string[8:])
            if(0<=int(string[:3])<256 and 0<=int(string[3:6])<256 and 0<=int(string[8:])<256):
                print(string[:3]+'.'+string[3:6]+'.'+string[6:8]+'.'+string[8:])

        elif(length_of_str==12):
            if(0<=int(string[:3])<256 and 0<=int(string[3:6])<256 and 0<=int(string[6:9])<256 and 0<=int(string[9:])<256):
                print(string[:3]+'.'+string[3:6]+'.'+string[6:])
            else:
                print("invalid ip")
    else:
        print("invalid input")


# get user input
ip_address = input("Enter a string : ")

stringToIP(ip_address)