# make a array of 6 x 6 as '*'
# 'A' is one player and 'B' is another player
# use random() module to get dice vaule
# player throw a dice twice of row and column
# 'A' -> 'B' toget point as 'A' = 1
# else initialize player
# get 5 points to win the game

import random
import time

# assign board as 2d array at the value of '*'
board = [['*' for i in range(6)] for i in range(6)]
# assign player variable for current player 
# initialy player 'A' throw the dice next player 'B'
currentplayer = 'B'
# assign scorea for player 'A' -> 0
scorea = 0
# assign scoreb for player 'B' -> 0
scoreb = 0

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
    for i in range(len(board)):
        for j in range(len(board[i])):
            # display the board
            print(board[i][j],' ',end='')
        print()

# build the function for switch player
def switchplayer(currentplayer):
    currentplayer = 'B' if (currentplayer=='A') else 'A'
    return currentplayer

# build the function for play the game
def playgame():
    global scorea
    global scoreb
    global currentplayer

    # call switchplayer() function to change player
    currentplayer = switchplayer(currentplayer)
    # print current player
    print("Player",currentplayer,"throw the dice",end=' ')
    # call throughdice() function get row and column    
    rows, colms = throughdice()

    if(board[rows][colms]=='A' and currentplayer=='B'):
        # change 'A' to 'B'
        board[rows][colms]=currentplayer
        # add score 1 to player 'B'
        scoreb+=1

    if(board[rows][colms]=='B' and currentplayer=='A'):
        # change 'B' to 'A'
        board[rows][colms]=currentplayer
        # add score 1 to player 'A'
        scorea+=1

    if board[rows][colms]=='*':
        # init current player
        board[rows][colms]=currentplayer



while True:
    # print the score 'A' and 'B'
    print("Player 'A' score is :",scorea)
    print("Player 'B' score is :",scoreb)
    
    # check anyone is won the match
    if(scorea==5):
        print("Player 'A' won the match")
        break
    if(scoreb==5):
        print("Player 'B' won the match")
        break
    
    # sleep 1s
    time.sleep(1)
    
    # call the playgame() function
    playgame()

    # # sleep 1s 
    time.sleep(1)

    displayboard()
    # sleep 1s
    time.sleep(1)