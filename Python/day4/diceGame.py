# Problem #2
# You have 6 x 6 game board where each cell is shown as a *
# This is a two player dice game. The die has numbers 1 to 6.
# Each player rolls the dice twice. First roll is row number, second roll is col number.
# After the player rolls the dice, in the (row,col) enter the player's initial. 
# If the player  A rolls the dice and  if  player B already has their initial in the same row,col
# add a point to A and change the initial to A. 

# Player who gets 5 points first wins the game.
# Print the board each time after the user rolls and also print the current score.
# Use functions
# 
# make a array of 6 x 6 as '*'
# 'A' is one player and 'B' is another player
# use random() module to get dice vaule
# player throw a dice twice of row and column
# 'A' -> 'B' toget point as 'A' = 1
# else initialize player
# get 5 points to win the game
# 

# import random and time module
import random
import time

# assign board as 2d array at the value of '*'
# board = [['*' for i in range(6)] for i in range(6)]
board = []
# assign player variable for current player 
# initialy player 'A' throw the dice next player 'B'
current_player = 'B'
# assign scorea for player 'A' -> 0
score_a = 0
# assign scoreb for player 'B' -> 0
score_b = 0

# build a method to make a board
def makeBoard(rows,clms):
    global board
    for row in range(rows):
        temp = []
        for col in range(clms):
            # add '*' into temp list
            temp.append('*')
        # add temp list into board
        board.append(temp)

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
    for row in range(len(board)):
        for col in range(len(board[row])):
            # display the board
            print(board[row][col],' ',end='')
        print()

# build the function for switch player
def switchplayer(currentplayer):
    # switch the player
    currentplayer = 'B' if (currentplayer=='A') else 'A'
    # return currentplayer
    return currentplayer

# build the function for play the game
def playgame():
    global score_a
    global score_b
    global current_player

    # call switchplayer() function to change player
    current_player = switchplayer(current_player)
    # print current player
    print("Player",current_player,"throw the dice",end=' ')
    # call throughdice() function get row and column    
    rows, colms = throughdice()

    if(board[rows][colms]=='A' and current_player=='B'):
        # change 'A' to 'B'
        board[rows][colms]=current_player
        # add score 1 to player 'B'
        score_b+=1

    if(board[rows][colms]=='B' and current_player=='A'):
        # change 'B' to 'A'
        board[rows][colms]=current_player
        # add score 1 to player 'A'
        score_a+=1

    if board[rows][colms]=='*':
        # init current player
        board[rows][colms]=current_player

# main method
def main():
    makeBoard(6,6)
    while True:
        # print the score 'A' and 'B'
        print("Player 'A' score is :",score_a)
        print("Player 'B' score is :",score_b)
        
        # check anyone is won the match
        if(score_a==5):
            print("Player 'A' won the match")
            break
        if(score_b==5):
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

# call main() method
main()