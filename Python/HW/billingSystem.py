# build application for restarent billing system
# 
# Add new items -> (eg: idly : 10rs)
# Cal bill for each customer based on their order
# Bill should include tax, tip 
# Ability to run promotion and give discount
# 
# menu_list = ["IDLY : 10","DOSA : 40","PONGAL : 50","POORI : 45","CHAPATHI : 45","TEA : 20","COFFEE : 20"]
# use "menu_list.txt" to store menu item and it's price
# 
# gst tax 8%
tax = 8
# discount 5%
discount = 5
# today collection
today_collection = 0
# current bill amount
total_price = 0 
# current bill list
bill_list = []


# discount calculation
def discountCalculation(price):
    price = round(price*(discount/100),2)
    print(" Your discount amount is = ",price,"Rs. ",sep='')
    return price

# tax calculation
def taxCalculation(price):
    price = round(price*(tax/100),2)
    print(" Your tax deduction is = ",price,"Rs. ",sep='')
    return price

# build functoin for today collection
def todayCollection():
    print("\n Today Total Collection : ",today_collection,' Rs. \n',sep='')

# build function for print bill
def printBill():
    print("\n---------------------------------------------")
    print("\n ~  Bill  ~  ")
    # print the dishes
    for i in bill_list:
        print(i)

# build function for get user input
def showOption():
    print("\n ~ Please Enter Your Option ~ \n")
    # option 1st is billing
    print(" 1. Calculate Billing. ")
    # option 2nd is menu list
    print(" 2. Menu List. ")
    # option 3rd is adin use
    print(" 3. Admin Use. ")
    # option 4th exit
    print(" 4. Exit. ")
    # get user input option
    option = int(input(" Enter your Option : "))
    # return option
    return option

# build display menu function
def displayMenu():
    print("\n ~ Select Your Dishe ~ \n")
    # open and read a file
    file = open("menu_list.txt",'r')
    rfile = file.read()
    menu_list = rfile.split(',')
    for i in range(len(menu_list)):
        j = menu_list[i].split(" ")
        print(' ',i+1,'. ',j[0],sep='')
    # close the file
    file.close()

# build display function for menu and price
def displayMenuPrice():
    # open menu_list file and read
    file  = open("./menu_list.txt",'r')
    rfile = file.read()
    # split into list
    menu_list = rfile.split(',')
    # menu_list.sort()
    print("\n ~ Available Dishes ~ \n")
    # display menu one by one
    for i in menu_list:
        i = i.split(" ")
        print(" ",i[0],"Rs.",i[2])
    print()
    # close the file
    file.close()

# build functio to edit only admin
def editing():
    while True:
        # option 1st is add new menu
        print(" 1. Add New Menu ")
        # option 2th is display menuwith price
        print(" 2. Menu with Price ")
        # option 3th is today collection
        print(" 3. Today Collection. ")
        # option 4th go back
        print(" 4. Back. ")
        # get user option
        option = int(input(" Enter your option : "))
        if(option==1):
            addMenu()
        elif(option==2):
            displayMenuPrice()
        elif(option==3):
            todayCollection()
        elif(option==4):
            # billingSystem()
            break
        else:
            print(" Enter valid option ")

# build add menu function
def addMenu():
    # get input from user for new menu
    new_menu = input(' Enter New Menu : ').upper()
    # get input from user for new menu price
    menu_price = input(" Enter price : ")
    # open menu_list file and append new menu
    menu_list = open("menu_list.txt",'a')
    # add new menu to menu_list file
    menu_list.write(","+new_menu+" : "+menu_price)
    # close the file
    menu_list.close()

# build function for admin
def adminUse():
    # get admin password from user
    passwrd = input(" Enter a Admin Password : ").lower()
    # verify adim
    if(passwrd=="admin"):
        editing()
    # if incorrect password
    else:
        print(" Please enter correct password ")
        adminUse()
        
# build price amount calculation function
def price_calculation(dishe,quantity):
    price = 0
    # open and read file
    file = open("menu_list.txt",'r')
    rfile = file.read()
    menu_list = rfile.split(',')
    menu = menu_list[dishe-1].split(" ")
    # price calculation
    price = int(menu[2])*quantity
    # print dish with price
    bill_list.append(" "+menu[0]+" "+menu[2]+" * "+str(quantity)+" = "+str(price)+" ")
    # return price
    return price

# build billing function
def billing():
    global today_collection
    global total_price
    # get input option from user
    dishe = int(input("\n Select dishe option : "))
    # get input quantity from user
    quantity = int(input(" Enter quantity : "))
    # config tto continue
    confirm = input(" Your are continue with billing (y/n) : ").lower()
    total_price = total_price + price_calculation(dishe,quantity)
    # yes to add amount to total price then get another input
    if(confirm=='y' or confirm=="yes"):
        billing()
    # no to return total price
    elif(confirm=='n' or confirm=='no'):
        # confirm you have any coupon code
        coupon_confirm = input(" You have any coupon (y/n) : ").lower()
        # check coupon
        if(coupon_confirm=='y' or coupon_confirm=='yes'):
            coupon = input(" Enter Coupon Code get discount : ").upper()
            # check coupon code and find total price
            if(coupon=="COUPON"):
                # call printbill() function
                printBill()
                # print total bill without tax and discount
                print(" Total Amount = ",total_price,"RS.")
                # total bill amount
                total_price = total_price + taxCalculation(total_price) - discountCalculation(total_price)
        # else calculate with tax
        else:
            # call printbill() function
            printBill()
            # print total bill without tax and discount
            print(" Total Amount = ",total_price)
            total_price = total_price + taxCalculation(total_price)
        # store bill amount to today collection
        today_collection = today_collection + total_price
        # clear bill list
        bill_list.clear()
        # print bill amount
        print(" Your Total Bill Amount is : ",total_price,"Rs. \n\n    ~ Thankyou For Your Visit ~ \n")
        print("---------------------------------------------")
        # return total price
        return total_price
        # break
    # for incvalid input
    else:
        billing()

# build function for restarent billing system
def billingSystem():
    while True:
        # call show option function
        option = showOption()
        # option 1 for billing
        if(option==1):
            displayMenu()
            billing()
        # option 2 for display memu
        elif(option==2):
            displayMenu()
        # option 3 for admin
        elif(option==3):
            adminUse()
        # option 4 for exit
        elif(option==4):
            todayCollection()
            break
        # for invaild input
        else:
            print(" Enter a valid option ")

# main function
def main():
    # greeting
    print("\n    ~ Wellcome!, My Restaurant ~    ")
    # call billing system
    billingSystem()

# call main function
main()