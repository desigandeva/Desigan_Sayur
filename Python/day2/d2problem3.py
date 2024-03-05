# roll the dicve continuously ( use random module )
# if rolled no is 0 game end
# if rolled no is even add 2 point
# if rolled no is odd then it's 1,3 for jump next move and 5 for add 3 point 
# point 50 reach game end

import random
import time

# assign point variable
point = 0

# roll the dice function 
def rolldice():
    dice_value = random.randrange(1,6)
    # print the rolled no
    print("Rolled no is :",dice_value)
    # return dice value
    return dice_value

# continuos loop
while True:
    # call rolldice() function
    dice_value = rolldice()
    
    # check dice value is even add 2 point
    if(dice_value%2==0):
        # add 2 points
        point+=2
    
    # check dice value is 1 or 3 jump to next move
    if(dice_value==1 or dice_value==3):
        print("Point is",point)
        # without adding any points move to next round       
        continue
    
    # check dice value is 5 add 3 point
    if(dice_value==5):
        # add 3 points
        point+=3
    
    # end the game if point reach 50 or get 0 from dice vvalue 
    if(dice_value==0) or (point>=50):
        print("Point is",point)
        print("game over")
        # to stop the entire program
        break

    # print the current point
    print("Point is",point)

    # loop take sleep for 2s
    time.sleep(2)


