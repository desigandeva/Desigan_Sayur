# build a parkinglot.
# get no of rows and columns from user.
# in a parkinglot
# 0  ->  available space
# other(carid)  ->   some one will be park the car
# entry of car entering and leaving
# make a charge of Rs 10, when it's leave the parking.

# init empty list for parkinglot
parkingLot = []
# assign parking charge is Rs. 10
parking_charge = 10
# calculate rotal collection
total_collection = 0

# display the parkinglot
def displayLot():
    print("\n * Parking Lot * \n")
    for row in range(len(parkingLot)):
        for col in range(len(parkingLot[row])):
            print(" ",parkingLot[row][col],end=' ')
        print()
    return 0

# print total collection
def collection():
    print("Total Collection Rs.",total_collection,'\n')
    
# display option for entering and leaving
def displayOption():
    displayLot()
    print("\n1. Entering Parking\n2. Leaving Parking\n3. Total collection\n")
    option = int(input("Enter your Option : "))
    if option==1:
        entryParking()
    if option==2:
        leaveParking()
    if option==3:
        collection()

# initialise parkinglot
def initParking():
    print("\n * Wellcome * \n")
    # get no of rows in parkinglot
    rows = int(input("Enter row : "))
    # get no of columns in parkinglot
    cols = int(input("Enter Column : "))
    # set parkinglot
    for row in range(rows):
        temp =[]         
        for col in range(cols):
            temp.append(0)
        parkingLot.append(temp)
    return 0

# entering to parkinglot
def entryParking(carId):
    for row in range(len(parkingLot)):
        for col in range(len(parkingLot[row])):
            if parkingLot[row][col] == 0:
                parkingLot[row][col] = carId
                print("Your Parling slot is",row,col)
                return 0
    # if 0 not in parkingLot:
    #     print("Sorry!, Parking is full..")
    #     return 1

# leaving from parkinglot
def leaveParking(carId):
    global total_collection
    for row in range(len(parkingLot)):
        for col in range(len(parkingLot[row])):
            if parkingLot[row][col] == carId:
                parkingLot[row][col] = 0
                total_collection += parking_charge
                print("Your parking charge is RS.",parking_charge,"\nThank You, for comming...")
                return 0

# main function
def main():
    initParking()
    # displayOption()
    while True:
            displayLot()
            print("\n1. Entering Parking\n2. Leaving Parking\n3. Total collection\n4. Exit\n")
            option = int(input("Enter your Option : "))
            if isinstance(option,int) and (0<option<5):
                if option==1:
                    carId = input("Enter your CarId (eg: a4) : ").lower()
                    if len(carId)==2:
                        entryParking(carId)
                    else:
                        print("Enter vaild CarId (eg: a4)")
                if option==2:
                    carId = input("Enter your CarId (eg: a4) : ").lower()
                    leaveParking(carId)
                if option==3:
                    collection()
                if option==4:
                    break
            else:
                print("Enter valid option!..")

# call main function
main()