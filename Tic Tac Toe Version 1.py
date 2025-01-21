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
def display(board):
    print(board)
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
            user_position = input(f"Player {player_num}, Your Shape: {user_shape}. Select a position 1-9 (type Q to quit) ")

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
        if b[2] == b[7] == b[12] == marker or b[18] == b[23] == b[28] == marker or b[34] == b[39] == b[44] == marker or b[2] == b[18] == b[34] == marker or b[7] == b[23] == b[39] == marker or b[12] == b[28] == b[44] == marker or b[2] == b[23] == b[44] == marker or b[12] == b[23] == b[34] == marker:
           return marker
        else:
            return None


# 5. Main function------------------------------------------------------------------------------------

def main():
    b = '["1", "2", "3"]\n["4", "5", "6"]\n["7", "8", "9"]'

    
    num_list = ["1","2","3","4","5","6","7","8","9"]
    player = 1
    shape_input = "Z"
    winner = None

    #There are only 9 possible squares
    for i in range(9):
        
        # Shows the updated board
        board = display(b)
        
        # Asks the user for the input position/quitting the game
        shape, position = user_input(num_list, player, shape_input)
        num_list.remove(position)
        shape_input = shape

        # Replaces the string int with the user's shape
        b = b.replace(f'{position}', f'{shape}')

        #Checks for a win
        winner = win_condition(b)

        #Ends game if winner is given. Also, it will break before we can switch the player.
        if winner != None:
            break


        #Switches player num
        if player == 1:
            player = 2
        elif player == 2:
            player = 1

        #Switches shape
        if shape_input == "O":
            shape_input = "X"
        elif shape_input == "X":
            shape_input ="O"

        print("___________________________________")
        print()

    #If all the numbers have been played and no one has won, it will call a tie.
    if not num_list and winner == None:
        print("\n"*10)
        print()
        print("___________________________________")
        display(b)
        print("Tie game")
        play()

    #Else it will call a winner.
    else:
        print("\n"*10)
        print()
        print("___________________________________")
        display(b)
        print(f"The winner is Player {player}, playing as shape {winner}")
        print()
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
# Make the interface better. Instead of having the numbers there, find a way to show the board without the numbers, and make the interface better.











        

        





