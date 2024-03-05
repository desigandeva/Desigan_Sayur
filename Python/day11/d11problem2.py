# get string value from user input
# change the given string to valid ip address

# build function for string to ip address
def stringToIP(string):
    lstr = len(string)
    # print(lstr)
    if(4<=lstr<=12):
        if(lstr==4):
            print(string[0]+'.'+string[1]+'.'+string[2]+'.'+string[3])
        elif(lstr==5):
            print(string[:2]+'.'+string[2]+'.'+string[3]+'.'+string[4])
            print(string[0]+'.'+string[1:3]+'.'+string[3]+'.'+string[4])
            print(string[0]+'.'+string[1]+'.'+string[2:4]+'.'+string[4])
            print(string[0]+'.'+string[1]+'.'+string[2]+'.'+string[3:])
        elif(lstr==6):
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

        elif(lstr==7):
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
        elif(lstr==8):
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
                
        elif(lstr==9):
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

        elif(lstr==10):
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

        elif(lstr==11):
            if(0<=int(string[:3])<256 and 0<=int(string[3:6])<256 and 0<=int(string[6:9])<256):
                print(string[:3]+'.'+string[3:6]+'.'+string[6:9]+'.'+string[9:])
            if(0<=int(string[2:5])<256 and 0<=int(string[5:8])<256 and 0<=int(string[8:])<256):
                print(string[:2]+'.'+string[2:5]+'.'+string[5:8]+'.'+string[8:])
            if(0<=int(string[:3])<256 and 0<=int(string[5:8])<256 and 0<=int(string[8:])<256):
                print(string[:3]+'.'+string[3:5]+'.'+string[5:8]+'.'+string[8:])
            if(0<=int(string[:3])<256 and 0<=int(string[3:6])<256 and 0<=int(string[8:])<256):
                print(string[:3]+'.'+string[3:6]+'.'+string[6:8]+'.'+string[8:])

        elif(lstr==12):
            if(0<=int(string[:3])<256 and 0<=int(string[3:6])<256 and 0<=int(string[6:9])<256 and 0<=int(string[9:])<256):
                print(string[:3]+'.'+string[3:6]+'.'+string[6:])
            else:
                print("invalid ip")
    else:
        print("invalid input")


# get user input
ip_address = input("Enter a string : ")

stringToIP(ip_address)