from random import randint

"""
Shell game (weak)
"""

def shell_game(): # Followed the pseudocode, could have been easier tho
    lst = ["A", "B", "C"]
    print("Voici le jeu du bonneteau, il y a trois bonneteaux: A, B et C, et sous l'un d'eux est caché une clé, vous avez deux essai pour trouver où se cache la clé.")
    print("Attention, en cas d'échec, la clé sera recachée.\n")
    att = 1

    won = 0 # Victory of the player variable

    while won == 0 and att <= 2:
        print("Essai numéro", att, ":")
        print("Choisissez un bonneteau :   A   B   C")
        guess = input("Votre réponse : ").upper()
        rdm = lst[randint(0,2)]
        if guess in lst:
            if guess == rdm:
                print("Votre instinct est bon, la clé était bien cachée sous le bonneteau", rdm)
                won = 1
                return True
            else:
                att += 1
                print("Votre instinct vous a trahi, la clé était cachée sous le bonneteau", rdm+". Vous perdez cet essai\n")
        else:
            print("Votre réponse n'est pas correcte, vous perdez cet essai.")
            att += 1
    print("Vous n'avez pas trouver la clé en deux essai, cette clé est donc perdue.")
    return False

"""
Rolling dice game (average)
"""

def roll_dice_game(): # Followed the pseudocode
    print("Bienvenue au jeu de dé, vous et le maître allez chacun votre tour lancer deux dés, le premier à obtenir un 6 gagne. Vous avez 3 essais.\n")

    won = 0 # Victory of the player variable
    att = 1 # Attempt number

    while won == 0 and att <= 3:
        print("Il vous reste", 4-att, "essais.\n")
        print("Appuyez sur 'entrée' pour lancer vos dés : ")
        input()
        dices = (randint(1,6), randint(1,6)) # Generates a tuple of 2 variables from 1 to 6
        print("Vous avez obtenu", dices[0], "et", dices[1])

        if 6 in dices:
            print("Vous avez donc gagné la partie et obtenez une clé")
            return True

        else:
            print("Vous n'avez pas de 6, c'est donc au maître de jouer\n")
            dices2 = (randint(1, 6), randint(1, 6)) # Generates a tuple of 2 variables from 1 to 6
            print("Le maître a obtenu", dices2[0], "et", dices2[1])

            if 6 in dices2:
                print("Le maître a donc gagné la partie et vous perdez la clé")
                return False
            else:
                att += 1
                print("Le maître n'as pas de 6 non plus, on passe donc au prochain tour.\n")

    print("Aucun de vous n'as gagné, vous n'obtenez donc pas de clé.")
    return False

"""
Chance challenge function
"""

def chance_challenge(): # Choose a random challenge from the math ones
    challenges = [shell_game, roll_dice_game]
    return challenges[randint(0,1)]()

chance_challenge()