# Parking garage problem
# 1.Write a program to calculate the revenue generated in a parking garage in a shopping mall
# 
# Parking fee is 
# If you return within 15 mins, its free
# Rs 100 for the first hr
# Rs 150 for each hr after that. 
# Fee is calculated in 30 min increments. (meaning, if you spent 25 mins, you will be charged for 30 mins
# If you spend 35 mins, you will be charged for one hr)
# Get entry time and exit time from customer as input and display the fee.
# 
# 2.same as above. End the program if 24hrs passes from when the first customer comes in. 
# Print the total fees collected.
# 
# 3. Same as above, adding more condition.
# The parking garage has 10 spaces numbered from 1 to 10.
# THere is a car entering or exiting every 10 mins.
# When a car enters, you need to tell them which lot is allotted for them.
# When the customer comes to pick up the car, get the lot number as input and calculate the fees.
# 
# Use arrays if needed.
# 
# 

# import time 
from datetime import datetime

# parking charges
# parking_Charge = [0,50,100,150]
# total collection
total_collection = 0
# particular person charge
charge = 0
# total parking garage
total_parking_garage = 10
# build parking garage 
parking_garage = [ slot+1 for slot in range(total_parking_garage)]
# parking slot
parking_slot = {}
# customer data
customer_data = {}

def currentTime():
    return datetime.now().strftime("%H:%M")

def totalCollection():
    print("Total Collection : ",total_collection)
    return 0

def cal_charge(entryTime,exitTime):
    entryHour, entryMin = map(int,entryTime.split(':'))
    exitHour, exitMin = map(int,exitTime.split(':'))
    parking_time = (exitHour*60+exitMin)-(entryHour*60+entryMin)
    total_hour = parking_time//60
    total_min = parking_time%60
    print("Total Parking hours is",total_hour,"hrs",total_min,"min")

    if(total_min>30):
        total_hour+=1
        if(total_hour<=1):
            charge = total_hour*100
        elif(total_hour>1):
            charge=((total_hour-1)*150)+100

    elif(15<total_min<=30):
        if(total_hour==0):
            charge=50
        elif(total_hour==1):
            charge=total_hour*100+50
        elif(total_hour>1):
            charge=((total_hour-1)*150)+100+50

    elif(total_min<=15):
        if(total_hour==0):
            charge=0
        elif(total_hour==1):
            charge=total_hour*100
        elif(total_hour>1):
            charge=((total_hour-1)*150)+100
    print("Your Parking Charge is ",charge,"Rs")
    return charge

def slotAllocate(user,entryTime):
    for slot in range(len(parking_garage)):
        if isinstance(parking_garage[slot],int):
            print(user,"your slot is",parking_garage[slot])
            parking_slot[parking_garage[slot]]={"User":user,"EntryTime":entryTime}
            parking_garage.remove(parking_garage[slot])
            return 0

def entryParking():
    user = input("Enter your name : ").capitalize()
    # entryTime = input("Enter a entry time (eg: 12:30) : ")
    entryTime = currentTime()
    slotAllocate(user,entryTime)
    return 0

def exitParking():
    global total_collection
    slot = int(input("Enter your slot : "))
    name = parking_slot[slot]["User"]
    entryTime = parking_slot[slot]["EntryTime"]
    # exitTime = input("Enter a exit time (eg: 16:30) : ")
    exitTime = currentTime()
    charge = cal_charge(entryTime,exitTime)
    total_collection+=charge
    customer_data[name]={"EnterTime":entryTime,"ExitTime":exitTime,"ParkingCharge":charge}
    parking_garage.append(slot)
    parking_slot.pop(slot)
    return 0

def end():
    first_customer = list(customer_data.keys())[0]
    fhour, fmin = map(int,customer_data[first_customer]["EntryTime"].split(':'))
    chour, cmin = map(int,currentTime().split(':'))
    return (fhour,fmin,chour,cmin)

def main():
    print(" * Parking Garage * \n")
    y=0
    while True:
        y+=1
        print(parking_garage,'\n',parking_slot,'\n',sep='')
        print("1. Entry Parking\n2. Exit Parking\n3. close")
        option = int(input("Enter your option : "))
        try:
            if(option==1):
                entryParking()
            elif(option==2):
                exitParking()
            elif(option==3):
                totalCollection()
                break
            else:
                print("Your option is out of range")
            if(y>12000):
                fhour,fmin,chour,cmin = end()
                if(fhour==chour and fmin==cmin):
                    break
        except Exception as e:
            print("Enter valid data",e)
    return 0

main()
