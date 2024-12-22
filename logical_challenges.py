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

    for i in range(3):

        # First check rows
        if sum(grid[i])/symbol == symbol: # If the statement is true, it means each case of the row is the symbol, so a win
            return True

        # Checks columns
        if sum([grid[j][i] for j in range(3)])/symbol == symbol: # If the statement is true, it means each case of the column is the symbol, so a win
            return True

    # Check diagonals
    if sum(grid[k][k] for k in range(3))/symbol == symbol or sum(grid[-l-1][-l-1] for l in range(3))/symbol == symbol:
        return True

    return False

# grids = [[1,2,3], [4,5,6], [7,8,9]]