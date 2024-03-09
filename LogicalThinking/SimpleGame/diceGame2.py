# Write an app for the follwoing two player game. You have a 6 x 6 board. 
# Users take turns rolling the dice twice. first roll is row no, second roll is col number. Mark the spot (row, col) as claimed by the user
# who rolled the dice.
# When the user rolls the dice within 1 col/row of a claimed spot of the other user, the other user gets a point. 
# If the spot is same as the claimed spot of the other user, the user that rolled the dice gets a point. 
# The player who gets 5 points first wins the game. 



import random
import time

# assign board as 2d array at the value of '*'
board = [['*' for i in range(6)] for i in range(6)]
# assign player variable for current player 
currentplayer = ''
# assign score 1st player -> 0
score_player1 = 0
# assign score 2nd player -> 0
score_player2 = 0

# build the function for throw the dice
def throughdice():
    # get random number between 1-6 using randint()
    rows = random.randint(1,6)
    colms = random.randint(1,6)
    print(rows,",",colms)
    # return row and column
    return(rows-1, colms-1)

# build the function for display the board in 6x6 array
def displayboard():
    print()
    for i in range(len(board)):
        for j in range(len(board[i])):
            # display the board
            print(board[i][j],' ',end='')
        print()
    print()

# build the function for switch player
def switchplayer(currentplayer):
    currentplayer = player2 if (currentplayer==player1) else player1
    return currentplayer

# build the function for play the game
def playgame():
    global score_player1, score_player2, currentplayer, player1, player2
    # call switchplayer() function to change player
    currentplayer = switchplayer(currentplayer)
    # print current player
    print("Player",currentplayer,"throw the dice",end=' ')
    # call throughdice() function get row and column    
    rows, colms = throughdice()

    if(board[rows][colms]==player1 and currentplayer==player2):
        # change
        board[rows][colms]=currentplayer
        # add score 1 to player2
        score_player2+=1

    if((board[rows][colms]==player2 and currentplayer==player1)):
        # change 
        board[rows][colms]=currentplayer
        # add score 1 to player1
        score_player1+=1

    if(colms<5):
        if(board[rows][colms+1]==player1 and currentplayer==player2):
            # add score 1 to player1
            score_player1+=1

        if((board[rows][colms+1]==player2 and currentplayer==player1)):
            # add score 1 to player2
            score_player2+=1


    if board[rows][colms]=='*':
        # init current player
        board[rows][colms]=currentplayer


def main():
    print("\n\t * Dice *\n")
    time.sleep(1.5)
    global currentplayer, player1, player2
    player1 = input("Enter 1st player name : ").capitalize()
    player2 = input("Enter 2nd player name : ").capitalize()
    currentplayer = player2
    print("\nWellcome , ",player1,"and",player2,"\nLoading...\n")
    time.sleep(2.5)
    print("Start \n")
    while True:
        # print the score 'A' and 'B'
        print("Player",player1,"score is :",score_player1)
        print("Player",player2,"score is :",score_player2)
        # check anyone is won the match
        if(score_player1==5):
            time.sleep(1.5)
            print("\nGame Over\nPlayer",player1,"won the match")
            break
        if(score_player2==5):
            time.sleep(1.5)
            print("\nGame Over\nPlayer",player2,"won the match")
            break
        
        # sleep 1s
        time.sleep(0.3)
        # call the playgame() function
        playgame()
        # # sleep 1s 
        time.sleep(0.3)
        # display board
        displayboard()
        # sleep 1s
        time.sleep(0.3)

# call main function
main()