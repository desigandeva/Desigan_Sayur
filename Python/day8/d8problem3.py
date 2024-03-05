# problem 3
# 
# VIP -> profit 30% of ticket price + Rs120 for every ticket sold.
# General -> profit 20% of ticket price + Rs80 for every ticket sold.
# Matinee -> profit 15% of the ticket price.
# subtracted 5% from ticket price for enetertinement tax
# 
# build function for profit calculation with 5% tax deduction
def profitWithTax(mclass,ticket_price):
    ticket_tax_price = ticket_price - ((ticket_price*5)/100)
    if(mclass=="vip"):
        ticket_price = (ticket_price*30/100) + ticket_tax_price
    elif(mclass=="general"):
        ticket_price = (ticket_price*20/100) + ticket_tax_price
    elif(mclass=="matinee"):
        ticket_price = (ticket_price*15/100) + ticket_tax_price
    return ticket_price


# build total collection function()
def totalCollection():
    # print greeting
    print("Wellcome!, to Theatre revenue ")

    # get vip ticket price
    vip_ticket_price = float(input("Enter Vip ticket price : "))
    # get no of vip ticket sold
    no_of_vticket =  int(input("Enter no of Vip ticket sold : "))
    # get general ticket price
    general_ticket_price = float(input("Enter General ticket price : "))
    # get no of general ticket sold
    no_of_gticket =  int(input("Enter no of General ticket sold : "))
    # get matinee ticket price
    matinee_ticket_price = float(input("Enter Matinee show ticket price : "))
    # get no of matinee ticket sold
    no_of_mticket =  int(input("Enter no of Matinee show ticket sold : "))

    # assign total collection initialy 0
    total_collection = 0

    # find total vip ticket price with profit
    total_collection = total_collection + (profitWithTax("vip",vip_ticket_price)*no_of_vticket)
    # find total general ticket price add to vip ticket price with profit
    total_collection = total_collection + (profitWithTax("general",general_ticket_price)*no_of_gticket)
    # find total matinee ticket price add with vip and general price with profit
    total_collection = total_collection + (profitWithTax("matinee",matinee_ticket_price)*no_of_mticket)

    # return the total collection
    return total_collection



# call total colletion function()
total_revenue = totalCollection()
# print total revenue with 5% tax deduction
print("Total revenue of this day ( with 5% tax deduction ) is :",total_revenue)
