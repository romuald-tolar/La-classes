class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self._titre = titre
        self._auteur = auteur
        self._nb_pages = nb_pages
        self._disponible = True

    def get_titre(self):
        return self._titre

    def set_titre(self, titre):
        self._titre = titre

    def get_auteur(self):
        return self._auteur

    def set_auteur(self, auteur):
        self._auteur = auteur

    def get_nb_pages(self):
        return self._nb_pages

    def set_nb_pages(self, nb_pages):
        if isinstance(nb_pages, int) and nb_pages > 0:
            self._nb_pages = nb_pages
        else:
            print("Erreur : le nombre de pages doit être un entier positif.")

    def verification(self):
        return self._disponible

    def emprunter(self):
        if self.verification():
            self._disponible = False
            print("Le livre a été emprunté.")
        else:
            print("Le livre n'est pas disponible.")

    def rendre(self):
        if not self.verification():
            self._disponible = True
            print("Le livre a été rendu.")
        else:
            print("Le livre n'a pas été emprunté auparavant.")
livre1 = Livre("Les Misérables", "Victor Hugo", 1488)
print(livre1.verification()) # affiche True
livre1.emprunter() # affiche "Le livre a été emprunté."
print(livre1.verification()) # affiche False
livre1.emprunter() # affiche "Le livre n'est pas disponible."
livre1.rendre() # affiche "Le livre a été rendu."
print(livre1.verification()) # affiche True
livre1.rendre() # affiche "Le livre n'a
