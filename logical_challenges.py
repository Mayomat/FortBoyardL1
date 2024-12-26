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

"""
Battleship game (High)
"""

def next_player(player):
    return [1,0][player] # Flex way to switch between 0 and 1

def empty_grid():
    return [[" ", " ", " "], # Initialize the grid
            [" ", " ", " "],
            [" ", " ", " "]]

def display_grid_ship(grid, message): # Display function
    print(message)
    print(f"{grid[0][0]} | {grid[0][1]} | {grid[0][2]}\n{grid[1][0]} | {grid[1][1]} | {grid[1][2]}\n{grid[2][0]} | {grid[2][1]} | {grid[2][2]}")
    print("---------")

def ask_position():

    play = input("Entrez la position (ligne, colonne) entre 1 et 3 (ex: 1,2) : ")
    valid = 0

    while not valid:  # Verify that the input is correct

        valid = (len(play) == 3 and play[0] in '123' and play[1] == ',' and play[2] in '123')  # Verify that the input is the correct format
        if not valid: # If input is incorrect, ask gain
            print("Position incorrecte, essayez encore :")
            play = input("Entrez la position (ligne, colonne) entre 1 et 3 (ex: 1,2) : ")

    return int(play[0]), int(play[2])

def initialize():

    boats = 2
    grid = empty_grid()

    while boats > 0: # While there is a boat to place

        # Ask the player where he wants to place his boat
        print("Où voulez-vous placer votre bateau ?")
        print("Bateau ", 3-boats) # Boat number
        coords = ask_position()

        if grid[coords[0]-1][coords[1]-1] == " ": # If the emplacement is free, place a boat
            grid[coords[0]-1][coords[1]-1] = "B"
            boats -= 1

        else:
            print("Emplacement incorrect, essayez encore.")

    display_grid_ship(grid, "Voici la grille de vos bateaux")
    return grid

def has_won(grid):
    return sum(grid[i][j] == "X" for i in range(3) for j in range(3)) == 2 # Check if there is two cross, is yes then there is a win

def turn(player, player_grid, player_shots_grid, opponent_grid): # Added player_grid, idk how else

    if player:

        print("Au maitre de jouer.")

        places = [(i,j) for i in range(3) for j in range(3) if player_grid[i][j] in [" ", "B"]] # Moves the master didnt already picked
        pick = places[randint(0, len(places)-1)] # Pick random place to shot
        print(f"Le maître tire en {pick[0]+1},{pick[1]+1}")

        if player_grid[pick[0]][pick[1]] == "B": # If the master shot a boat, place an X on the player grid
            player_grid[pick[0]][pick[1]] = "X"
            print("Touché ! Vous perdez un bateau.")

        else: # If the master shot a boat, place a dot (.) on the player grid
            player_grid[pick[0]][pick[1]] = "."
            print("Plouf, le maître vous a raté.")

        display_grid_ship(player_grid, "Voici la grille de vos bateaux")

    else:

        print("A vous de jouer.")
        pos = ask_position()
        print(f"Vous tirez en {pos[0]},{pos[1]}")

        if opponent_grid[pos[0]-1][pos[1]-1] == "B": # If you shot a boat, add an X on your shot grid
            player_shots_grid[pos[0]-1][pos[1]-1] = "X"
            print("Touché ! Vous coulez un bateau.")

        else: # If you missed, add a dot on your shot grid
            player_shots_grid[pos[0]-1][pos[1]-1] = "."
            print("Plouf... vous avez raté.")

        display_grid_ship(player_shots_grid, "Voici la grille de vos tirs")

def master_initialize():

    grid = empty_grid()
    places = [(i, j) for i in range(3) for j in range(3)] # Every usable place for the boats
    boat1 = places.pop(randint(0, len(places)-1)) # Take a random localisation and removes it from the usable places
    boat2 = places[randint(0, len(places)-1)] # Take a random localisation from the usable ones

    # Places the boats on the randomly chosen positions
    grid[boat1[0]][boat1[1]] = "B"
    grid[boat2[0]][boat2[1]] = "B"

    return grid

def battleship_game():

    print("Vous et le maître allez chacun avoir une grille 3x3 où seront placés 2 bateaux.\n"
          "Chacun votre tour, vous aller entrer des coordonnées pour tenter de couler les bateaux adverses.\n"
          "Le premier qui coule les deux bateaux de son adversaire remporte la victoire.")

    # Initialise grids for the player and the master
    player_grid = initialize()
    player_shots_grid = empty_grid()
    master_grid = master_initialize()

    player = 0 # 0:Player, 1:Master

    while not (has_won(player_grid) or has_won(player_shots_grid)): # While none has won

        turn(player, player_grid, player_shots_grid, master_grid) # Do a turn
        player = next_player(player) # Switch player turn

    if player: # Determine who won, the winner is the inverse from player since we switched after the end of the round
        print("Vous avez coulé tous les bateaux du maître ! Vous remporter cette épreuve et obtenez un clé.")
        return True
    else:
        print("Tous vos bateaux ont été coulés par le maître. Vous perdez cette épreuve et n'obtenez pas de clé.")
        return False

battleship_game()