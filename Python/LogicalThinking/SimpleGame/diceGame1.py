# Two player dice game.
# Each player will roll the die (numbers from 1 to 6)
# Points are added to each roll.
# 1 - 1 pt
# 2 - 5 pts
# 3 - 15 pts
# 4 - (-15) pts
# 5 - (-5) pts
# 6 - (-1) pts
# 
# Find which player scores 100 first and how many time they had to roll the die.
# Hint - use random numbers to generate the die (no need to get user input)
# Use Arrays and while loop.
# 
# 


import time
import random

# points list
points = [1,5,15,-15,-5,-1]
# player1 score
player1_score = 0
# player2 score
player2_score = 0
# current player
current_player = ''
# player1 turn
player1_turns = 0
# player1 turn
player2_turns = 0

def switchPlayer(current_player):
    if current_player == player1:
        current_player = player2
    else:
        current_player = player1
    return current_player

def rollDice():
    return random.randint(0,5)

def calScore(current_player,score):
    global player1_score,player2_score,player1_turns,player2_turns
    if current_player==player1:
        player1_score+=score
        player1_turns+=1
    elif current_player==player2:
        player2_score+=score
        player2_turns+=1

def main():
    print("\n\t * Roll a Dice * \n")
    global current_player,player1,player2
    time.sleep(1)
    # player1
    player1 = input(" Enter a 1st player name : ").capitalize()
    # player2
    player2 = input(" Enter a 2nd player name : ").capitalize()
    current_player = player2
    print("\n Wellcome , ",player1,"and",player2,"\n Loading....")
    time.sleep(2.5)
    print(" Game Started ")
    while True:
        print(player1,"Score : ",player1_score)
        print(player2,"Score : ",player2_score)
        if(player1_score>=100):
            time.sleep(1.5)
            print('\n Game Over \n Congratulation',player1,"\n You won the match in",player1_turns,"turns\n")
            break
        elif(player2_score>=100):
            time.sleep(1.5)
            print('\n Game Over \n Congratulation',player2,"\n You won the match in",player2_turns,"turns\n")
            break
        current_player = switchPlayer(current_player)
        dice = rollDice()
        calScore(current_player,points[dice])
        print('\n',current_player,"will roll",dice+1)
        time.sleep(0.5)
    
main()