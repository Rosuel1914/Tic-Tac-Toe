# The difference between Tic Tac Toe V1 and V2 is that V2
# 1. Has a cleaner interface
# 2. Win condition isn't hard coded
# 3. There is a function for alternating the player, it's not longer in the main func
# 4. There is a function for alternating the shape, it's no longer in the main func
# 5. Cleans up the tie game condition in the main func
# 6. Cleans up the declaring of a winner in the main func
# 7. Removed the '1-9' from "Select a position 1-9"

import sys


# 1. Asks the user if he wants to play-------------------------------------------------------
def play():
    play = "Wrong Val"
    
    while play.lower() not in ["y", "n"]:
        play = input("Would you like to play Tic-Tac-Toe?(Y or N) ").lower()
        

    if play.lower() == 'n':
        print("\nGame End")
        sys.exit()
    else:
        print("\nLet's Begin\n")
        main()



# 2. Displaying Board------------------------------------------------------
def display(board_nums):
    
    p = f' {board_nums[1]} | {board_nums[2]} | {board_nums[3]} \n---------\n {board_nums[4]} | {board_nums[5]} | {board_nums[6]} \n---------\n {board_nums[7]} | {board_nums[8]} | {board_nums[9]} \n'
    
    print(p)
    print()




# 3. Asking for user input--------------------------------------------------------------------------

def user_input(position_list, player_num, shape):
    # Asking for the shape
    valid_shape = False
    valid_position = False
    valid_input = False

    p = position_list
    s = shape


    while valid_input == False:
        
        while valid_shape == False:

            # If a valid shape is passed, we don't have to ask the user anymore. This is used because we only want to ask the shape once.
            if s.upper() in ["X", "O"]:
                user_shape = s.upper()
                break

            
            #Asks for the user's shape
            user_shape = input(f"Player 1: Select X or O? (type Q to quit) ")
            print()

            if user_shape.upper() in ["X", "O"]:
                user_shape = user_shape.upper()
                valid_shape = True

            elif user_shape.upper() == "Q":
                print("\nGame end")
                sys.exit()

            else:
                 print("Not an acceptable shape")
                 print()
            
        while valid_position == False:
            #Asks for which position they want
            user_position = input(f"Player {player_num}, Your Shape: {user_shape}. Select a position on the board.(type Q to quit) ")

            if user_position.isdigit() and 0 < int(user_position) < 10 and user_position in p:
                valid_position = True
               

            elif user_position.upper() == "Q":
                print("\nGame end")
                sys.exit()
                
            else:
                print("Not an acceptable position")
                print()

        #Lmao... Make sure this is indented properly. You made a mistake where it wasn't indented properly, and it never broke out of the while loop for valid_input
        valid_input = True

    print()
            


    return user_shape, user_position



# 4. Win condition

def win_condition(board):
    b = board

    for marker in ["X", "O"]:
        #Checks any of the 8 possible win conditions
        if b[1] == b[2] == b[3] == marker or b[4] == b[5] == b[6] == marker or b[7] == b[8] == b[9] == marker or b[1] == b[5] == b[9] == marker or b[3] == b[5] == b[7] == marker or b[1] == b[4] == b[7] == marker or b[2] == b[5] == b[8] == marker or b[3] == b[6] == b[9] == marker:
           return marker
        else:
            return None

# 6. Switches player numbers and shapes

def switch(p,s):
    if p == 1 and s == 'X':
        return 2,'O'
    elif p == 1 and s == 'O':
        return 2,'X'
    elif p == 2 and s == 'X':
        return 1, 'O'
    else:
        return 1,'X'
    
# 5. Main function------------------------------------------------------------------------------------

def main():
    
    #This will be passed to the display() function. We have a dummy value '1' because indexing starts at 0 and I wanted to simplify it.
    board = ['1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    #These are the valid index values. If the user chooses a a number from this list, it will be deleted so that you can't play the same number twice.  
    num_list = ["1","2","3","4","5","6","7","8","9"]

    #By default, player 1 always goes first
    player = 1

    #This is a default invalid shape input
    shape_input = "Z"

    #By default, there is no winner. Once a winner is decided, this will change.
    winner = None

    #There are only 9 possible squares to choose from, so we are iterating 9 times.
    for i in range(9):
        
        # Shows the updated board
        display(board)
        
        # Asks the user for the input position
        shape, position = user_input(num_list, player, shape_input)

        #Removes the position so that you can't use it twice.
        num_list.remove(position)
        shape_input = shape

        # Replaces the position chosen with the shape for that player.
        board[int(position)] = shape

        #Checks for a win
        winner = win_condition(board)

        #Ends game if winner is given. Also, it will break before we can switch the player.
        if winner != None:
            break

        #Switches Player and shape every turn
        player, shape_input= switch(player, shape_input)

        print("___________________________________")
        print()


    #Displays the board for a final time once the game has ended
    display(board)
    
    #Checks for a tie game or winner.
    if winner != None:

        #If winner is not None, then that means someone won because the loop was broken
        print(f"The winner is Player {player}, playing as shape {winner}")

    else:

        #If we exited the loop but winner == None, then that means the for loop finished its 9 iterations and the game is a tie.
        print("Tie Game")

    print()
    #Play again?
    play()
        

play()







# To-Do list/ To fix list.
# ------------------
# Core Parts
# 1. Asks if they want to start the game
# 2. Display the board/updated board
# 3. Asks the user for the shape and position
# 4. Win Condition function
# 5. Game phase/Main



# Bugs fixed/features added:
# 1. Make it so that you only ask player 1 for which shape they want to choose. After that, only choose the position.
# 2. Alternate between player 1 and player 2.
# 3. Tie condition
# 4. Make sure that you can't choose the same position twice.
# 5. Game would end prematurely. It would ask for user input, and then do nothing. --> this was an indentation error.
# 6. In the event that it took 9 turns, make sure the final board is shown
# 7. Make sure that if X is chosen first, it will alternate to O. Vice Versa

# The only thing missing is a win/tie function Edit: This is complete


#Pending
# Make the interface better. Instead of having the numbers there, find a way to show the board without the numbers, and make the interface better. Edit: Complete











        

        





