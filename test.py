def test():
	print('Ceci est un test*')

def bisextile():
	annee = input('Saissisez l\'année que vous voulez verifier : ')
	annee = int(annee)
	if annee%4 == 0:
		if annee%100 == 0:
			if annee%400 == 0:
				print('Annee bisextile en vue')
			else:
				print('Ce n\'est pas une année bisexetile :(')
		else:
			print('Année bisextile en vue !')
	else:
		print('Ce n\'est pas une année bisextile :(')

bisextile()
