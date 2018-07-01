#Programme de pendu
import pickle

# Class : Joueur, dico-pendu
class player:
    PLAYERS = {}
    INSTANCE = 0
    APPEL = 0
    def __init__(self):

        if not player.PLAYERS:
            player.APPEL += 1
            print(player.APPEL)
            player.PLAYERS = player.loadClass()
            # print(cls.PLAYERS['Ludovic'].items())
            #PLAYERS = {
            #    'Ludovic': {'score': 1, 'parties': 1},
            #    'Alan': {'score': 78, 'parties': 45},
            #}
        #cls.INSTANCE += 1



    @classmethod
    def loadClass(cls):
        with open('save/personnage.sav', 'rb') as fichier:
            monPickle = pickle.Unpickler(fichier)
            requete = monPickle.load()
            return requete

    @classmethod
    def saveClass(cls, tableau):
        with open('save/personnage.sav', 'wb') as fichier:
            monPickle = pickle.Pickler(fichier)
            monPickle.dump(tableau)

bertrand = player()


#for name, value in player.PLAYERS['Ludovic'].items():
#    print(name)
#    print(value)

jacob = player()

# Premiere mission : ecrire les bases du programmes



# => L'identification / enregistrement

# Le joueur choisi un pseudo
# S'il existe dans la bdd, on lui demande un password
# S'il n'existe pas, on lui demande un password mais on l'enregistre

# => Un menu, qui permet d'acceder à trois catégories

#### Ajout de mots au dictionnaire

#### Consulter les scores (classement)

#### Jouer !
tableau = {
    'Ludovic': {'score': 1, 'parties': 1},
    'Alan': {'score': 78, 'parties': 45},
    'George': {'score': 782, 'parties': 7478},
}

for key, value in tableau.items():
    if key == 'Ludovic':
        test = value
        print(key)
        print('\n')
        for key2, value2 in test.items():
            print(key2)
            print(value2)
player.saveClass(tableau)
