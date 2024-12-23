from random import randint

"""
Game of Nim (weak)
"""

def display_sticks(n): # Prints n sticks
    if n > 0:
        print("Batons restants : ", " | " * n)
    else:
        print("Batons restants : aucun, la partie est terminée.")

def player_removal(n):

    ans = input("Combien de batons voulez-vous retirer ? (1 2 3) : ")

    while True:
        try:
            ans = int(ans)
            if ans in [1, 2, 3]: # Verify that the answer is correct, type, correct number
                break
            else :
                ans = input("Cette réponse n'est pas valide, essayez encore :")
        except ValueError: # If not, ask again
            ans = input("Cette réponse n'est pas valide, essayez encore :")

    return n-ans

def master_removal(n):
    return n%4

def nim_game():
    sticks = 20
    turn = 0

    print("Sur 20 bâtons, vous pourrez chacun votre tour retirer 1 2 ou 3 bâtons, celui qui retire le dernier bâton perds.")
    display_sticks(sticks)

    while sticks > 0:
        print("Au tour du maître, " if turn else "A vous de jouer, ")
        if turn == 0: # If player turns
            sticks = player_removal(sticks) # Removes the sticks of the player
            display_sticks(sticks)
            turn = 1 # Change turn
        else:
            rm = master_removal(sticks) # Removed the sticks of the master
            print("Le maître enlève ", rm, "bâtons")
            sticks -= rm
            display_sticks(sticks)
            turn = 0 # Change turn

    if turn: # Since after each play we change turn, results are inverted
        print("Vous avez pris le dernier bâton, vous avez la partie et n'obtenez pas de clé.")
        return False
    else:
        print("Le maître a pris le dernier bâton, vous avez gagné la partie et obtenez une clé.")
        return True

"""
Tic Tac Toe (medium)
"""

def display_grid(grid):
    print(f"{grid[0][0]} | {grid[0][1]} | {grid[0][2]}\n---------\n{grid[1][0]} | {grid[1][1]} | {grid[1][2]}\n---------\n{grid[2][0]} | {grid[2][1]} | {grid[2][2]}")

def check_victory(grid, symbol):

    """
    Logic explanation :
    You check the sum of the acsii value (ord(x)) of the row / col / diag and divide by the ascii value of the symbol.
    If you get 3, it means the row / col / diag is composed of 3 times the symbol, so it is a victory.
    """

    for i in range(3):

        # First check rows
        if sum(ord(j) for j in grid[i])/ord(symbol) == 3: # If the statement is true, it means each case of the row is the symbol, so a win
            return True

        # Checks columns
        if sum(ord(grid[k][i]) for k in range(3))/ord(symbol) == 3: # If the statement is true, it means each case of the column is the symbol, so a win
            return True

    # Check diagonals
    if sum(ord(grid[k][k]) for k in range(3))/ord(symbol) == 3 or sum(ord(grid[2-l][l]) for l in range(3))/ord(symbol) == 3:
        return True

    return False

def master_move(grid, symbol, advsymbol): # Return the master's move

    available_moves = []

    # Check for every case if it is empty
    for i in range(3):
        for j in range(3):
            if grid[i][j] == " ":
                available_moves.append((i, j))

    block = 0 # Variable to change if you can block the player from winning

    # For every empty case, look what the plays do
    for move in available_moves:

        # Create the new grid if move is played
        grid2 = [row[:] for row in grid] # Needed gpt there, idk why but modifying grid2 changed grid, with grid2 = grid.copy() too
        grid2[move[0]][move[1]] = symbol

        # Look if this play makes a win for the master
        if check_victory(grid2, symbol):
            return move
        # Look if this play makes a win for the player, if yes, consider blocking
        grid2[move[0]][move[1]] = advsymbol
        if check_victory(grid2, advsymbol):
            block = move

    # If there is no possible victory but a block is found, play it
    if block != 0:
        return block

    # If there is no win or block play, play randomly
    return available_moves[randint(0, len(available_moves)-1)]

def player_turn(grid): # Return the grid after the player play

    play = input("A vous de jouer, où voulez vous placer votre symbol ? (ex: 1,2) : ")
    valid = 0

    while not valid: # Verify that the input is correct

        valid = (len(play) == 3 and play[0] in '123' and play[1] == ',' and play[2] in '123') # Verify that the input is the correct format

        if valid: # If the format is correct

            play = (int(play[0]), int(play[2]))  # Put the input into a tuple

            # Check that the spot is empty and playable
            if grid[play[0]-1][play[1]-1] == " ":
                valid = 1
            # If not, then the input is not valid
            else:
                play = input("Votre emplacement est déjà occupé, essayez encore (ex: 1,2) : ")
                valid = 0

        else:  # If not, then the input is not valid
            play = input("Votre emplacement est incorrect, essayez encore (ex: 1,2) : ")

    grid[play[0]-1][play[1]-1] = "X" # Change the case where the player played
    return grid

def full_grid(grid): # Return if the grid is full
    for i in range(3): # In each row
        if " " in grid[i]: # Check if there is an empty space
            return False # If there is, the grid is not full
    return True # Otherwise, the grid is full

def check_result(grid): # Check if the game is finished
    if check_victory(grid, "X"): # Check if player "X" won
        return True
    if check_victory(grid, "O"): # Check if player "O" won
        return True
    if full_grid(grid): # Check if there is no move left
        return True
    return False

def tictactoe_game(): # Operates the whole game

    print("Bienvenue à l'épreuve du morpion, tentez de remporter une clé en vainquant le Maître ! ")

    grid = [[" ", " ", " "], # Initialize the grid
            [" ", " ", " "],
            [" ", " ", " "]]
    display_grid(grid)

    turn = 0

    while not check_result(grid): # While the game is not finished

        if turn == 0: # If it is the player turn
            player_turn(grid)
            display_grid(grid)
            if check_victory(grid, "X"): # If player won, return True
                return True
            else: # Otherwise switch turns
                turn = 1

        else:
            move = master_move(grid, "O", "X") # Get the move of the master
            grid[move[0]][move[1]] = "O" # Apply it on the grid
            print("Au maître de jouer (O)...")
            display_grid(grid)
            if check_victory(grid, "O"): # If master win, return False
                return False
            else: # Otherwise switch turns
                turn = 0

    return False

print(tictactoe_game())