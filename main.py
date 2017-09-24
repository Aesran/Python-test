# FIchier principal du jeu
# Boucle qui continue tant qu'on a pas decide de quitter le jeu
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
joueur.monargent()


continuer = True
while continuer:
    key = input("Utilisez la commande @quit pour quitter le jeu")
    key = key
    if key == '@quit':
        continuer = False
    if not continuer:
        break

    #Si le joueur a miser ->


    # Si le joueur n'as ni miser, ni quitter ->
