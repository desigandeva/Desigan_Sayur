# Amusement Park
# get name and dob from user
# 0-18 and 60> -> 50.Rs
# 18-50 -> 75.Rs
# 20% discount in total cost-> tue and thur 
# 
# 

# import class in datetime module 
from datetime import datetime,date,time,timedelta

# today collection
today_collecttion = 0


def ticketPrice(age):
    if (age>=60 or 0<age<19):
        return 50
    elif (18<=age<60):
        return 75

def discount():
    today = datetime.now().strftime('%A')
    if today == "Tuesday" or today == "Thursday":
        return 20
    else:
        return 0

def findAge(dob):
    try:
        date_format = "%d-%m-%Y"
        yob = datetime.strptime(dob, date_format).year
        current_year = date.today().year
        age = current_year - yob
        return age
    except Exception as e:
        print(e)

def totalCost(price):
    global total_cost
    total_cost += price

def todayCollection(ticketPrice):
    global today_collecttion
    today_collecttion += (ticketPrice-(ticketPrice*(discount()/100)))
    return today_collecttion

def printTicket(visiter_count, child, adult):
    print()
    if(visiter_count==(child+adult)):
        if(child==0):
            print('-'*50,"\n\t\t * Wellcome * \n")
            print("\t  Adults    -> ",adult,'*',75,'=',adult*75)
            print('\t'*3,"Total =",total_cost,'\n')
            discount_cost = total_cost * (discount()/100)
            print("\tToday discount is",discount(),'%\n\tYour discount amount is',discount_cost,'Rs')
            print("\tFinal Cost : ",total_cost-discount_cost,"Rs\n\n\t * Thank you for comming... * \n",'-'*50)

        elif(adult==0):
            print('-'*50,"\n\t\t * Wellcome * \n")
            print("Child / Senior Citizen  -> ",child,'*',50,'=',child*50)
            print('\t'*3,"    Total =",total_cost,'\n')
            discount_cost = total_cost * (discount()/100)
            print("\tToday discount is",discount(),'%\n\tYour discount amount is',discount_cost,'Rs')
            print("\tFinal Cost : ",total_cost-discount_cost,"Rs\n\n\t * Thank you for comming... * \n",'-'*50)
        
        else:
            print('-'*50,"\n\t\t * Wellcome * \n")
            print("Child / Senior Citizen  -> ",child,'*',50,'=',child*50)
            print("Adults                  -> ",adult,'*',75,'=',adult*75)
            print('\t'*3,"    Total =",total_cost,'\n')
            discount_cost = total_cost * (discount()/100)
            print("\tToday discount is",discount(),'%\n\tYour discount amount is',discount_cost,'Rs')
            print("\tFinal Cost : ",total_cost-discount_cost,"Rs\n\n\t * Thank you for comming... * \n",'-'*50)
    print()
    return 0


def getUserData():
    child_count = 0
    adult_count = 0
    print()
    no_of_visiter = int(input("Enter no of visiter's : "))
    for user in range(no_of_visiter):
        user_name = input("Enter your name : ")
        dob = input("Enter your date of birth (DD-MM-YYYY) : ")
        age = findAge(dob)
        totalCost(ticketPrice(age))
        if(0<age<19 or age>=60):
            child_count += 1
        elif(18<=age<60):
            adult_count += 1
    printTicket(no_of_visiter, child_count, adult_count)

def main():
    while True:
        # total ticket cost
        global total_cost
        total_cost = 0
        print("\n1. Entry Ticket\n2. Exit\n")
        try:
            option = int(input("Enter your option : "))
            option = int(option)
            if(option==1):
                getUserData()

            elif(option==2):
                print("\nToday total collection :",today_collecttion,'Rs')
                break

            else:
                print("Enter valid option")

        except Exception as e:
            print('\n',e)
            main()

        todayCollection(total_cost)





print("\n\t* Amusement Park *\n")
# call main function
main()


