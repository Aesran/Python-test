from tkinter import *

class Interface(Frame):

    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""

    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=1200, height=800, **kwargs)
        self.pack(fill=BOTH)
        self.nb_clic = 0

        # Création de nos widgets
        self.message = Label(self, text="Vous n'avez pas cliqué sur le bouton.")
        self.message.pack()
        self.boutton = []
        nombre = 0
        while nombre < 11:


            self.boutton.append(Button(self, text=nombre))
            self.bouton_current = self.boutton[nombre]
            self.bouton_current.pack(side="left")
            nombre += 1

        self.bouton_quitter = Button(self, text="Quitter", command=self.quit)
        self.bouton_quitter.pack(side="left")

        self.bouton_cliquer = Button(self, text="Cliquez ici", fg="red",
                command=self.cliquer)
        self.bouton_cliquer.pack(side="right")

    def cliquer(self):
        """Il y a eu un clic sur le bouton.

        On change la valeur du label message."""

        self.nb_clic += 1
        self.message["text"] = "Vous avez cliqué {} fois.".format(self.nb_clic)


fenetre = Tk()
fenetre.geometry("600x600")

interface = Interface(fenetre)


interface.mainloop()

interface.destroy()
