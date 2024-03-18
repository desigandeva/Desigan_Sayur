# Problem #3
# Its is a single player game where the user starts with 0 points. User keeps rolling the 
# dice.If the rolled number is 0, game ends. If the rolled number is even, then 2 points are
#  added. If the number is odd, then if the number is 1,3 then the user has to jump. 
#  If the number is 5, then 3 points are added. The game ends when the user has 50 points.
# 
# roll the dicve continuously ( use random module )
# if rolled no is 0 game end
# if rolled no is even add 2 point
# if rolled no is odd then it's 1,3 for jump next move and 5 for add 3 point 
# point 50 reach game end
# 

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

# build a main() method
def main():
    # print roll the dice
    print("\n\t * Roll the Dice * \n")
    # sleep 1s
    time.sleep(1)
    # print game start
    print(" Game Start \n")
    # sleep 0.5s
    time.sleep(0.5)
    # print loading
    print(" Loading....\n")
    # sleep 1s
    time.sleep(1)
    # continuos loop
    global point
    while True:
        time.sleep(0.5)
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

# call main() function
main()