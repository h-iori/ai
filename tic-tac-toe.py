import os
import time

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player = 1

########win Flags##########
Win = 1
Draw = -1
Running = 0
Stop = 1
###########################
Game = Running
Mark = 'X'

# This Function Draws the Game Board
def DrawBoard():
    print(" %c | %c | %c " % (board[1], board[2], board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))
    print(" | | ")

# This Function Checks if the position is empty or not
def CheckPosition(x):
    return board[x] == ' '

# This Function Checks if the player has won or not
def CheckWin():
    global Game

    # Horizontal winning condition
    if board[1] == board[2] == board[3] != ' ':
        Game = Win
    elif board[4] == board[5] == board[6] != ' ':
        Game = Win
    elif board[7] == board[8] == board[9] != ' ':
        Game = Win
    # Vertical Winning Condition
    elif board[1] == board[4] == board[7] != ' ':
        Game = Win
    elif board[2] == board[5] == board[8] != ' ':
        Game = Win
    elif board[3] == board[6] == board[9] != ' ':
        Game = Win
    # Diagonal Winning Condition
    elif board[1] == board[5] == board[9] != ' ':
        Game = Win
    elif board[3] == board[5] == board[7] != ' ':
        Game = Win
    # Match Tie or Draw Condition
    elif all(board[i] != ' ' for i in range(1, 10)):
        Game = Draw
    else:
        Game = Running

print("Tic-Tac-Toe Game")
print("Player 1 [X] --- Player 2 [O]\n")
print("\nPlease Wait...")
time.sleep(1)

while Game == Running:
    os.system('cls')
    DrawBoard()

    if player % 2 != 0:
        print("Player 1's chance")
        Mark = 'X'
    else:
        print("Player 2's chance")
        Mark = 'O'

    choice = int(input("Enter the position between [1-9] where you want to mark: "))
    
    if 1 <= choice <= 9 and CheckPosition(choice):
        board[choice] = Mark
        player += 1
        CheckWin()

os.system('cls')
DrawBoard()

if Game == Draw:
    print("Game Draw")
elif Game == Win:
    player -= 1
    if player % 2 != 0:
        print("Player 1 Won")
    else:
        print("Player 2 Won")
