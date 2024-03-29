# Play the game Rock Papar Scissors with the computer.
# Play it three times and best of three wins. 
# If you win, print your name in color (look for a python package to do this)
# Hint - Use random number generation

import random
import time

# for computer from this list
system_choice = ["Rock","Paper","Scissor"]


def play():
    player_score = 0
    turn = 0
    while turn<3:
        try:
            print("\n\t * Round",turn+1,'*\n')
            time.sleep(0.3)
            system = random.choice(system_choice)
            print("1. Rock\n2. Paper\n3. Scissor")
            option = input("Enter your option : ")
            option = int(option)
            if(0<option<4):
                if(option==1 and system=="Scissor"):
                    player_score+=1
                elif(option==2 and system=="Rock"):
                    player_score+=1
                elif(option==3 and system=="Paper"):
                    player_score+=1
                turn+=1
            else:
                print("Your option out of range, Please enter  1 to 3 \n")
        except Exception as e:
            print("Enter valid option",e,'\n')
        time.sleep(0.5)
    return player_score

print("\n\t * Rock - Paper - Scissor * \n")
time.sleep(1)
player_name = input(" Enter your name : ").capitalize()
time.sleep(0.05)
print(" Wellcome",player_name,'\n Loading....')
time.sleep(2.5)
print(" Game will Started ")
score = play()
time.sleep(0.3)
print(" Game Over ")
if(score>=2):
    print('\n Congratulations ',player_name,'\n',"You win the game and your score is",score)
else:
    print('\n Sorry!..',player_name,'\n',"You loss the game and your score is",score)
