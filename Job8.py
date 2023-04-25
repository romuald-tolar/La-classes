class Livre:
    def __init__(self, titre: str, auteur: str, nb_pages: int):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages

    def get_titre(self) -> str:
        return self.__titre

    def set_titre(self, titre: str) -> None:
        self.__titre = titre

    def get_auteur(self) -> str:
        return self.__auteur

    def set_auteur(self, auteur: str) -> None:
        self.__auteur = auteur

    def get_nb_pages(self) -> int:
        return self.__nb_pages

    def set_nb_pages(self, nb_pages: int) -> None:
        if nb_pages > 0:
            self.__nb_pages = nb_pages
        else:
            print("Le nombre de pages doit être un entier positif.")

    def __str__(self) -> str:
        return f"{self.__titre} écrit par {self.__auteur}, {self.__nb_pages} pages."
# Création d'un livre
livre1 = Livre("Les Misérables", "Victor Hugo", 1488)

# Affichage des attributs du livre
print(livre1.get_titre())      # "Les Misérables"
print(livre1.get_auteur())     # "Victor Hugo"
print(livre1.get_nb_pages())   # 1488

# Modification du titre et du nombre de pages du livre
livre1.set_titre("Notre-Dame de Paris")
livre1.set_nb_pages(656)

# Affichage des attributs du livre modifié
print(livre1.get_titre())      # "Notre-Dame de Paris"
print(livre1.get_nb_pages())   # 656

# Tentative de modification du nombre de pages avec une valeur invalide
livre1.set_nb_pages(-42)       # affiche "Le nombre de pages doit être un entier positif."
print(livre1.get_nb_pages())   # 656
