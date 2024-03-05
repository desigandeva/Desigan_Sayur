# first class -> profit 25% of the price + Rs100 for every ticket
# Second class -> profit 15% of the price + Rs70 for every ticket 
# Third class (i don't know if there is a third class) -> profit 5% of the price.
# Get the price and no of tickets sold for each class and calculate the total profit. 
# 
# build function for profit calculation
def profitCal(rclass,ticket_price):
    # for first calss 25% profit and RS 100 for every ticket extra
    if rclass == "first_class":
         ticket_price = ((ticket_price-100)*100)/125
         profit_price = ticket_price*(25/100)+100
    # for first calss 15% profit and RS 70 for every ticket extra
    elif rclass == "second_class":
         ticket_price = ((ticket_price-70)*100)/115
         profit_price = ticket_price*(15/100)+70
    # for first calss 5% profit
    elif rclass == "third_class":
         ticket_price = (ticket_price*100)/105
         profit_price = ticket_price*(5/100)
    # return the ticket price
    return ticket_price, profit_price

# build function for railway total collect
def railwayTotalProfit():
    # print greeting
    print("Wellcome!, to railway collection ")

    # get first class ticket price
    first_class = float(input("Enter 1st Class Ticket Price : "))
    # get no of tickets sold in first class
    no_of_fclass = int(input("Enter no of Ticket sold in 1st Class : "))
    # get second class ticket price
    seond_class = float(input("Enter 2nd Class Ticket Price : "))
    # get no of tickets sold in second class
    no_of_sclass = int(input("Enter no of Ticket sold in 2nd Class: "))
    # get third class ticket price
    print("Enter '0' for no 3rd class")
    third_class = float(input("Enter 3rd Class Ticket Price : "))
    # check third class is there
    if(third_class!=0):
        # get no of tickets sold in third class
        no_of_tclass = int(input("Enter no of Ticket sold in 3rd Class : "))

    # assign total collection initialy 0
    total_collection = 0
    # assign profit collection initialy 0
    profit_collection = 0

    # find first class profit, class pofitCal() function add the profit to total collection 
    ticket, profit = profitCal("first_class",first_class)
    # total collection
    total_collection = total_collection + (first_class*no_of_fclass)
    # profit collection
    profit_collection = profit_collection + (profit*no_of_fclass)

    # find second class profit, class pofitCal() function add the profit to total collection 
    ticket, profit = profitCal("second_class",seond_class)
    # total collection
    total_collection = total_collection + (seond_class*no_of_sclass)
    # profit collection
    profit_collection = profit_collection + (profit*no_of_sclass)

    # check if third class is there
    if(third_class!=0):
        # find third class profit, class pofitCal() function add the profit to total collection
        ticket, profit = profitCal("third_class",third_class) 
        # total collection
        total_collection = total_collection + (third_class*no_of_tclass)
        # profit collection
        profit_collection = profit_collection + (profit*no_of_tclass)

    # return the total collection
    return total_collection,profit_collection

# call the railway total collection function
total,profit = railwayTotalProfit()
# print total collection
print("Total Collection :",total)
# print total profit
print("Total Profit :",profit)