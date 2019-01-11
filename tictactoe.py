import os
import random

os.system("color 3")
os.system("cls")

#Global variable assignments
game_board = ['  1  |', '  2  |', '  3  ', '\n', '  4  |', '  5  |', '  6  ' , '\n', '  7  |', '  8  |', '  9  ']
cur_move = 0
set_turn_o = False

#Let player1 choose what marker to use
def choose_marker():
    player1 = input("Player1: Choose X or O: ").upper()
    player2 = ''
    if player1.upper() == 'X':
        return ('X', 'O')
    elif player1.upper() == 'O':
        return ('O','X')    
    else:
        print("ERROR, WRONG CHARACTER ASSIGNED!")
        quit()

#Function to print game_board that we assigned before
def game_play(board):
    print(''.join(board))

#Check if there is a winner
def check_winner(game_board, player):
    #Clear the console and re-print a fresh version of the game_board
    os.system("cls")
    game_play(game_board)

    #Check all the positions in the game_board for potential winner
    return ((game_board[0] == f"  {player}  |" and game_board[1] == f"  {player}  |" and game_board[2] == f"  {player}  ") or
    (game_board[4] == f"  {player}  |" and game_board[5] == f"  {player}  |" and game_board[6] == f"  {player}  ") or
    (game_board[8] == f"  {player}  |" and game_board[9] == f"  {player}  |" and game_board[10] == f"  {player}  ") or
    (game_board[0] == f"  {player}  |" and game_board[5] == f"  {player}  |" and game_board[10] == f"  {player}  ") or
    (game_board[2] == f"  {player}  " and game_board[5] == f"  {player}  |" and game_board[8] == f"  {player}  |") or
    (game_board[0] == f"  {player}  |" and game_board[4] == f"  {player}  |" and game_board[8] == f"  {player}  |") or
    (game_board[1] == f"  {player}  |" and game_board[5] == f"  {player}  |" and game_board[9] == f"  {player}  |") or
    (game_board[2] == f"  {player}  " and game_board[6] == f"  {player}  " and game_board[10] == f"  {player}  ")) 

#The main game function
def game(player, move, cur_player):
    global game_board
    start_player = ''

    #Check who is the starting player
    if cur_player == 1:
        starting_player = "Player 1"
    elif cur_player == 2:
        starting_player = "Player 2"

    #If statement to make sure starting player gets a unique starting string
    if move == 1:
        player_move = int(input(f"{starting_player} is starting, choose position for {player}: "))
    else:
        player_move = int(input(f"{starting_player} choose position for {player}: "))

    # Checks if a marker is already in specified position (Doesn't have to check for the first move thus using move > 1)
    if move > 1:
        if player_move < 4:
            if game_board[player_move - 1] != f"  {player_move - 1}  |" or game_board[player_move - 1] != f"  {player_move - 1}  ":
                player_move = int(input(f"Already taken! Choose new position for {player}: "))
        elif player_move > 3 and player_move < 7:
            if game_board[player_move] != f"  {player_move}  |" or game_board[player_move] != f"  {player_move}  ":
                player_move = int(input(f"Already taken! Choose new position for {player}: "))
        else:
            if game_board[player_move + 1] != f"  {player_move + 1}  |" or game_board[player_move + 1] != f"  {player_move + 1}  ":
                player_move = int(input(f"Already taken! Choose new position for {player}: "))

    #Placing markers depending on number assigned by user to game_board, indexing is a bit weird due to \n in the list
    if player_move < 4:
        if player_move == 3:
            game_board[player_move - 1] = f"  {player}  "
        else:    
            game_board[player_move - 1] = f"  {player}  |"
    elif player_move > 3 and player_move < 7:
        if player_move == 6:
            game_board[player_move] = f"  {player}  "
        else:
            game_board[player_move] = f"  {player}  |"
    else:
        if player_move == 9:
            game_board[player_move + 1] = f"  {player}  "
        else:
            game_board[player_move + 1] = f"  {player}  |"

#Assign marker type to player1 and player2 (Search up Tuple unpacking for people that don't get how this work)
player1, player2 = choose_marker()
#Choose a random player to start the game
start_player = random.randint(0, 1)

#Infinite loop to run the game
while True:
    os.system("cls")
    game_play(game_board)
    cur_move += 1
    # Check who is the starting player and make sure it doesn't allow player1 to set 
    # marker 2 times after eachother if player1 is starting player
    if start_player == 0 and cur_move == 1:
        game(player1, cur_move, 1)
        set_turn_o = True
    elif start_player == 1 and cur_move == 1: 
        game(player2, cur_move, 2)
    else:
        if set_turn_o:
            set_turn_o = False
        else:
            game(player1, cur_move, 1)
        #Check if player1 did a winning move
        if check_winner(game_board, player1):
            print(f"Winner is Player 1 ({player1}), Congratulations!")
            quit()
        #Clear the console window and print a fresh game_board with the new marker set by player 1
        os.system("cls")
        game_play(game_board)
        cur_move += 1

        #Call the main game function with player set to player 2
        game(player2, cur_move, 2)

        #Check if player2 did a winning move
        if check_winner(game_board, player2):
            print(f"Winner is Player 2 ({player2}), Congratulations!")
            quit()
        
        #Game is a tie if amount of moves reach 9 due to no winning move and all spots being taken
        if cur_move == 9 and not check_winner(game_board, player1) and not check_winner(game_board, player2):
            os.system("cls")
            game_play(game_board)
            print("It's a TIE!")
            quit()