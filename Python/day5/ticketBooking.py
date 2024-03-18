# Problem #1
# Wrote a program for seat reservation in a theatre.
# You can decide on the configuaration of the seats (no of rows and no of seats in each row, and a passage in between)
# When the user asks for tickets, you need to provide them tickets in the form of seat no.
# For eg, User ask for 3 seats in the middle. Output is F11, F12 , F13
# Print the theatre configuaration at the end of each transaction.
# 
# Problem #2
# Same problem as above. Also calculate tickets price. 
# Firsrt 3 rows - Rs100
# Rows 4 to 12 - Rs 200
# Rows 13 till top - Rs 300.
# 3 seats close to the wall on both sides costs less than the other seats in the same row.
# 
# assign seat capacity
# 1 - 3 row ticket price -> 100
# 4 - 12 row ticket price -> 200
# 13 - top row (15) ticket price -> 300 
# each row has 30 seats
# total seats -> 15 * 30 -> 450
# ticket price for 3 seats closed to the both wall is 10% discount from the same row ticket price
# 

import time

# define seat
# oseat = [["0".join(chr(65+i)+str(j+1)) if j<9 else chr(65+i)+str(j+1) for j in range(30)] for i in range(15)]
seat = []
# ticket booked
seatbooked =  "   " # None # "[B]"
# 1st class ticket price
firstclass = 300
# 2nd class ticket price
secondclass = 200
# 3rd class ticket price
thirdclass = 100

# make seat availability
def makeSeatAvailability(rows,cols):
    for row in range(rows):
        temp = []
        for col in range(cols):
            # make seat value
            if col<9:
                temp.append("0".join(chr(65+row)+str(col+1)))
            else:
                temp.append(chr(65+row)+str(col+1))
        # add row
        seat.append(temp)

# build a function for display the seat availabilty
def displayseat():
    print("\nSeat Availability\n")
    for row in range(len(seat)):
        for col in range(len(seat[row])):
            # print the seat number
            print(seat[row][col],' ',end='')
        print('')
    print('\n')


# build ticket booking function
def bookticket(ticket):
    for row in range(len(seat)):
        for col in range(len(seat[row])):
            # print(seat[row][col])
            # book the seat
            if(seat[row][col]==ticket):
                print("Ticket Sucessfully Booked :",ticket)
                # ticket_price = ticketprice(ticket)
                seat[row][col]=seatbooked
                # for first 3 rows
                if(row<3):
                    # for corner 3 seat
                    if(col<3 or col>len(seat[row])-3):
                        ticket_price = discountprice(thirdclass)
                    else:
                        ticket_price = thirdclass
                # for row 4 to 12
                if(row>=3 and row<12):
                    # for corner 3 seat
                    if(col<3 or col>len(seat[row])-3):
                        ticket_price = discountprice(secondclass)
                    else:
                        ticket_price = secondclass
                # last 3 rows
                if(row>=12):
                    # for corner 3 seat
                    if(col<3 or col>len(seat[row])-3):
                        ticket_price = discountprice(firstclass)
                    else:
                        ticket_price = firstclass
                return ticket_price
            # check seat is availabal or not
            # if(seat[row][col]==seatbooked):
            #     print("Seat already Booked\n")
    return 0
            

# build discountprice() for discount the corner seats 
def discountprice(price):
    # 10% discount from orginal price
    return (price-(price*10/100))


def main():
    makeSeatAvailability(15,30)
    while True:
        # call the displayseat() function
        displayseat()
        # total ticket price
        totalprice = 0
        # get seat no from user
        try:
            # get ticket number from user
            tickets_list = input("Enter seat no (seperate by ,):").split(',')
            print('')

            for ticket in range(len(tickets_list)):
                # make seat number as perfect number
                if(len(tickets_list[ticket])==2):
                    tickets_list[ticket]="0".join(tickets_list[ticket].upper())
                else:
                    tickets_list[ticket]=tickets_list[ticket].upper()
                # print(tickets_list[ticket])
                # call the bookticket() function to make booking
                ticket_price = bookticket(tickets_list[ticket])
                #  add ticketprice to totalprice
                totalprice += ticket_price
                # sleep 3s
                time.sleep(3)
            
            # print the total tickets price
            print("Total Ticket Price is :", totalprice)
            # sleep 2s
            time.sleep(2)
        
        except Exception as e:
            print(e)

# call main() function
main()