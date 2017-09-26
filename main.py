
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
while continuer:
    print("Bienvenu dans le Casino d'Aesran")
    print("A tout moment, vous pouvez utiliser la commande @quit pour quitter")
    print("Le but de ce jeu est de trouver la bonne valeur de la roulette,")
    print("Ou au moins sa couleur (rouge pour un chiffre pair, noir pour impair)")
    print("Entrez simplement des chiffres pour miser !")
    print("###########################################")

    print("Vous avez ", joueur.argent ," euros en banque")

    key_test = int('machin')
    print(type(key_test))
    key = input()

    if key == '@quit':
        continuer = False
    if not continuer:
        break

    #Si le joueur a miser ->
    if isinstance(key, int):
        print("c'est un nombre !")

    # Si le joueur n'as ni miser, ni quitter ->
    else:
        print("Vous n'avez ni miser, ni quitter, alors on fait quoi ?!!")
