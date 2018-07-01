import math

def VolumeCone(rayon,hauteur):
    """Fonction qui calcul le volume d'un cone, sans arrondir.
    Mais le resultat est limité à deux chiffres après la virgule"""
    volume = math.pi * (rayon * rayon) * hauteur / 3
    volume = (int(volume*100))
    volume = volume/100
    return volume

def TVA_defaut(prix):
    """Prend un prix hors-taxe et y ajoute la TVA de 20%"""
    tva = 20 # taxe de 20%
    prix_tva = prix * tva / 100
    prix_tva = prix + prix_tva
    return prix_tva

def somme(*param):
    """A partir d'une liste, calcul la somme de tous les chiffres entrées
    récupère également les resultats supérieur à 100 et le nombre de données"""
    tour = 0
    nombreSup = 0
    varSomme = 0
    for entree in param:
        tour += 1
        if entree >= 100:
            nombreSup += 1
        varSomme += entree

    return({"nombreSup": nombreSup, "somme": varSomme,"nombreDeDonnee": tour})


def CombienDiviser2(nombre):
    resultat = int(nombre)
    tour = 0
    while resultat%2 == 0:
        tour += 1
        resultat = resultat / 2
    return(tour)

def HauteurParcourue(nombreMarche, hauteurMarche):
    hauteur = (hauteurMarche * nombreMarche) * 2
    distanceParcourue = (hauteur * 5) * 7
    distanceParcourue = distanceParcourue/1000
    print('Pour ' , nombreMarche , ' marches de ' , hauteurMarche , 'cm de hauteur, le gardien parcourt ' , distanceParcourue , 'm de hauteur.' )

def Amende(poule,chien,vache,ami):
    taux = int((poule + (chien * 3) + (vache * 5) + (ami * 10) - 100)/100)
    print(taux)
    return taux*200


print(Amende(52,45,10,15))



HauteurParcourue(2000,15)
