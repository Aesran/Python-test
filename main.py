
# fonction primaires
# fonction qui permet de verifier la couleur d'un chiffre
import sys
import random
import time

print(sys.version_info)
def quelleCouleur(value):
    if value%2 == 0:
        return 'rouge'
    else:
        return 'noire'





# CLASSE UTILISÉE POUR LE JEU
class player:
# Attributs
  def __init__(self, somme):
    print(somme)
    self.argent = somme
    self.mise = 0
    self.couleur = 'rouge'
    self.chiffre = 0
    self.nom = 'Joueur'
    print(self.argent)

  def monargent(self):
        print(self.argent)





# DEBUT DU PROGRAMME
joueur = player(100)


# Boucle qui continue tant qu'on a pas decide de quitter le jeu
continuer = True
partie = 0
while continuer:
    if partie == 0:
        print("Bienvenu dans le Casino d'Aesran")
        print("A tout moment, vous pouvez utiliser la commande @quit pour quitter")
        print("Le but de ce jeu est de trouver la bonne valeur de la roulette,")
        print("Ou au moins sa couleur (rouge pour un chiffre pair, noir pour impair)")
        print("Entrez 'miser' pour miser !")

    partie += 1
    print(partie)

    print("###########################################")
    print("Vous avez ", joueur.argent ," euros en banque")


    key = input('=. ')

    if key == '@quit':
        continuer = False

    #Si le joueur a miser ->
    if key == 'miser':
        print("Sur quel chiffre voulez vous miser ? De 1 à 50")
        miseChiffre = int(input('=. '))
        print('Combien voulez-vous misez ?')
        print('Il vous reste', joueur.argent , ' euros en banque')
        miseArgent = int(input('=. '))
        print('Bien vous êtes prêt ? C\'est partit !')
        # on choisi un nombre au hazard entre 1 et 50
        hazard = random.randint(1,50)
        # on annonce que la roulette tourne (et on fait patienter quelques secondes)
        print('La roue tourne ...')
        time.sleep(1)


        # Puis on lances les conditions !
        if hazard == miseChiffre:
            nb = miseArgent * 2
            joueur.argent += nb
            print('Jackpot ! Vous gagnez ' , nb , ' euros')
        elif quelleCouleur(miseChiffre) == quelleCouleur(hazard):
            print('Même couleur, vous gardez votre mise')
        else:
            print('Perdu ! Vous perdez la mise')
            joueur.argent = joueur.argent - miseArgent
            if joueur.argent <= 0:
                print("Vous n'avez plus d'argent, le jeu s'arrête")
                break

        # Si le chiffre est le même, sinon si le chiffre est de même couleur, sinon on perd tout



    if not continuer:
        break
