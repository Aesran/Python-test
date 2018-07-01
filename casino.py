
# Casino roulette

# Importation des modules nécéssaires

import random # Pour générer un nombre aléatoire
import time # Pour générer un temps de latence quand la roulette est lancée

# Fonctions
def quelleCouleur(value): # On détermine la couleur du chiffre 'value'
    if value%2 == 0: # Si le reste de value divisé par deux est égal à 0, le chiffre est pair
        return 'rouge'
    else: # Sinon, il est impair.
        return 'noire'

# Variable de jeu
argent = 100



# Boucle qui continue tant qu'on a pas decide de quitter le jeu
continuer = True
partie = 0
while continuer:
    if partie == 0: # Si le jeu vient d'être lancé
        print("Bienvenu dans le Casino d'Aesran")
        print("A tout moment, vous pouvez utiliser la commande 'quitter' pour quitter")
        print("Le but de ce jeu est de trouver la bonne valeur de la roulette,")
        print("Ou au moins sa couleur (rouge pour un chiffre pair, noir pour impair)")
        print("Entrez 'miser' pour miser !")

    partie += 1 # On incrémente, pour comptabiliser le nombre de partie


    print("###########################################")
    print("Vous avez ", argent ," euros en banque")

    key = input('=. ') # On demande à l'utilisateur de faire un choix

    if key == 'quitter': # S'il choisi de quitter
        continuer = False

    #Si le joueur a miser ->
    if key == 'miser': # S'il choisi de miser
        miseChiffre = 789

        while miseChiffre > 50: # Tant que la mise ne se situe pas entre ce qui est demandé
            print("Sur quel chiffre voulez vous miser ? De 1 à 50")
            miseChiffre = input('=. ')

        print('Combien voulez-vous misez ?')
        print('Il vous reste', argent , ' euros en banque')
        miseArgent = input('=. ')
        print('Bien vous êtes prêt ? C\'est partit !')
        # on choisi un nombre au hazard entre 1 et 50
        hazard = random.randint(1,50)
        # on annonce que la roulette tourne (et on fait patienter quelques secondes)
        print('La roue tourne ...')
        time.sleep(1)


        # Puis on lances les conditions !
        if hazard == miseChiffre:
            nb = miseArgent * 2
            argent += nb
            print('Jackpot ! Vous gagnez ' , nb , ' euros')
        elif quelleCouleur(miseChiffre) == quelleCouleur(hazard):
            print('Même couleur, vous gardez votre mise')
        else:
            print('Perdu ! Vous perdez la mise')
            argent = argent - miseArgent
            if argent <= 0:
                print("Vous n'avez plus d'argent, le jeu s'arrête")
                break
    else: # Le joueur n'as rien choisi, on lui rappelle donc les commandes puis la boucle reprend
        print('Choisissez entre "miser" ou "quitter"')



    if not continuer:
        break
