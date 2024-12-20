from random import randint

"""
Factorial Challenge (Weak)
"""

def factorial(n): # Factorial of n function computation
    if n == 0 or n == 1: # Special case, 1 and 0 returns 1
        return 1
    else:
        fact_n = 1
        for i in range(2,n+1): # Factorial computation
            fact_n = fact_n * i
    return fact_n

def math_challenge_factorial(): # First math challenge, find the factorial
    rdm = randint(1, 10) # Random number from 1 to 10
    result = factorial(rdm) # Factorial of the random number to guess

    print("Votre épreuve est simple, tentez de trouver la factorielle du nombre suivant :", rdm, "\n")

    guess = input("Votre réponse : ")
    while True:
        try: # Verify if the number in an integer
            int(guess)
            break
        except ValueError: # If not, ask again
            guess = input("Voyons, ceci n'est pas une réponse valide, essayez encore : ")

    guess = int(guess) # Transform into int to compare

    if guess == result: # Check if answer is right
        print("Gagné(à implanter)")
        return True
    else:
        print("Perdu (à implanter)")
        return False


"""
Linear equation test (weak)
"""

def solve_linear_equation():
    x_coef = randint(1,10) # Random number for the coefficient of x
    const = randint(1,10) # Random number for the constant
    x_sol = -const/x_coef # Calculation of the solution
    return x_coef,const,x_sol

def math_challenge_equation():
    x_coef,const,x_sol = solve_linear_equation()

    print("Votre épreuve est simple, tentez de trouver la solution de l'équation suivante :", str(x_coef)+"x", "+", const, "= 0", "\n")

    guess = input("Votre réponse : ")
    while True:
        try:
            float(guess)
            break
        except ValueError:
            guess = input("Voyons, ceci n'est pas une réponse valide, essayez encore : ")

    guess = float(guess)  # Transform into int to compare

    if guess == x_sol:  # Check if answer is right
        print("Gagné(à implanter)")
        return True
    else:
        print("Perdu (à implanter)")
        return False