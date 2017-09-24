# FIchier principal du jeu
# Boucle qui continue tant qu'on a pas decide de quitter le jeu

continuer = True
while continuer:
    key = input("Utilisez la commande @quit pour quitter le jeu")
    key = key
    if key == '@quit':
        continuer = False
    if not continuer:
        break
