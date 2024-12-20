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
    x_sol = round(-const/x_coef, 2) # Calculation of the solution
    return x_coef, const, x_sol

def math_challenge_equation():
    x_coef,const,x_sol = solve_linear_equation()

    print("Votre épreuve est simple, tentez de trouver la solution de l'équation suivante :", str(x_coef)+"x", "+", const, "= 0", "\n")

    guess = input("Votre réponse (arrondir à 2 unités): ")

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


"""
Prime number challenge (average)
"""

def is_prime(n):
    divisors = [] # List fo the divisors of n
    for i in range(1,n+1): # From one to n, if "i" is a divisor of n, add it to the list
        if n % i == 0:
            divisors.append(i)
    return len(divisors) == 2 # A number is prime is it is only divisible by 1 and itself, so there is two divisors

def nearest_prime():
    number = randint(10, 20) # Generates the number for which we want the closest prime number
    nearest = [] # Nearest prime numbers
    i,j = number, number # Iterates through the neighbors of our random number

    while len(nearest) == 0: # While we don't find any prime numbers
        if is_prime(i): # If lower number is prime, add it to the list
            nearest.append(i)
        else: # If not, decrease the cursor
            i -= 1
        if is_prime(j): # If upper number is prime, add it to the list
            nearest.append(j)
        else: # If not, increase the cursor
            j += 1

    return number, nearest

def math_challenge_prime():
    number, nearest = nearest_prime()

    print("Votre épreuve est simple, tentez de trouver le nombre premier le plus proche du nombre suivant :", number, "\n")

    guess = input("Votre réponse : ")

    while True:
        try:
            int(guess)
            break
        except ValueError:
            guess = input("Voyons, ceci n'est pas une réponse valide, essayez encore : ")

    guess = int(guess)  # Transform into int to compare

    if guess in nearest:  # Check if answer is right
        print("Gagné(à implanter)")
        return True
    else:
        print("Perdu (à implanter)")
        return False


"""
Math roulette challenge (average)
"""

def math_roulette_challenge():
    roulette = [randint(1,20) for _ in range(5)] # Create a list of five random numbers from 1 to 20
    operation = randint(1,3) # Random variable for the operation choice
    result = 1

    if operation == 1: # 1 for the addition of each number
        result = sum(roulette) # Compute the sum of the list
        print("Votre épreuve est simple, tentez de trouver la combinaison de ces nombres par l'addition :", roulette, "\n")

    if operation == 2: # 2 for the subtraction of each number
        result = roulette[0] - sum(roulette[1:]) # Subtraction of all numbers is just the first one minus the sum of the others
        print("Votre épreuve est simple, tentez de trouver la combinaison de ces nombres par la soustraction :", roulette, "\n")

    if operation == 3: # 3 for the multiplication of each number
        for n in roulette: # Multiply each number in the list by each-other
            result *= n
        print("Votre épreuve est simple, tentez de trouver la combinaison de ces nombres par la multiplication :", roulette, "\n")

    guess = input("Votre réponse : ")

    while True:
        try:
            int(guess)
            break
        except ValueError:
            guess = input("Voyons, ceci n'est pas une réponse valide, essayez encore : ")

    guess = int(guess)  # Transform into int to compare

    if guess == result:  # Check if answer is right
        print("Gagné(à implanter)")
        return True
    else:
        print("Perdu (à implanter)")
        return False


"""
Math challenge function
"""

def math_challenge(): # Choose a random challenge from the math ones
    challenges = [math_challenge_factorial, math_challenge_equation, math_challenge_equation, math_roulette_challenge]
    return challenges[randint(0,3)]()

math_challenge()