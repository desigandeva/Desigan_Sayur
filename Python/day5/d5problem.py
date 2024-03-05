# assign seat capacity
# 1 - 3 row ticket price -> 100
# 4 - 12 row ticket price -> 200
# 13 - top row (15) ticket price -> 300 
# each row has 30 seats
# total seats -> 15 * 30 -> 450
# ticket price for 3 seats closed to the both wall is 10% discount from the same row ticket price

import time

# define seat
oseat = [["0".join(chr(65+i)+str(j+1)) if j<9 else chr(65+i)+str(j+1) for j in range(30)] for i in range(15)]
seat = oseat
# ticket booked
seatbooked =  "   " # None # "[B]"
# 1st class ticket price
firstclass = 300
# 2nd class ticket price
secondclass = 200
# 3rd class ticket price
thirdclass = 100

# build a function for display the seat availabilty
def displayseat():
    print("\nSeat Availability\n")
    for i in range(len(seat)):
        for j in range(len(seat[i])):
            print(seat[i][j],' ',end='')
        print('')
    print('\n')


# build ticket booking function
def bookticket(ticket):
    for i in range(len(seat)):
        for j in range(len(seat[i])):
            # print(seat[i][j])
            # book the seat
            if(seat[i][j]==ticket):
                print("Ticket Sucessfully Booked :",ticket)
                # ticket_price = ticketprice(ticket)
                seat[i][j]=seatbooked
                # for first 3 rows
                if(i<3):
                    # for corner 3 seat
                    if(j<3 or j>len(seat[i])-3):
                        ticket_price = discountprice(thirdclass)
                    else:
                        ticket_price = thirdclass
                # for row 4 to 12
                if(i>=3 and i<12):
                    # for corner 3 seat
                    if(j<3 or j>len(seat[i])-3):
                        ticket_price = discountprice(secondclass)
                    else:
                        ticket_price = secondclass
                # last 3 rows
                if(i>=12):
                    # for corner 3 seat
                    if(j<3 or j>len(seat[i])-3):
                        ticket_price = discountprice(firstclass)
                    else:
                        ticket_price = firstclass
                return ticket_price
            # check seat is availabal or not
            # if(seat[i][j]==seatbooked):
            #     print("Seat already Booked\n")
    return 0
            

# build discountprice() for discount the corner seats 
def discountprice(price):
    # 10% discount from orginal price
    return (price-(price*10/100))



while True:
    # call the displayseat() function
    displayseat()
    # total ticket price
    totalprice = 0
    # get seat no from user
    try:
        ticket = input("Enter seat no (seperate by ,):").split(',')
        print('')

        for x in range(len(ticket)):
            if(len(ticket[x])==2):
                ticket[x]="0".join(ticket[x].upper())
            else:
                ticket[x]=ticket[x].upper()
            # print(ticket[x])
            # call the bookticket() function to make booking
            ticket_price = bookticket(ticket[x])
            totalprice += ticket_price
            # sleep 3s
            time.sleep(3)
        
        # print the total ticket price
        print("Total Ticket Price is :", totalprice)
        # sleep 2s
        time.sleep(2)
    
    except Exception as e:
        print(e)