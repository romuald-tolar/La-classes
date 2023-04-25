class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def get_longueur(self):
        return self.__longueur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur
# Créer un rectangle avec une longueur de 10 et une largeur de 5
rect = Rectangle(10, 5)

# Afficher les attributs du rectangle
print("Longueur :", rect.get_longueur())
print("Largeur :", rect.get_largeur())

# Modifier la longueur et la largeur du rectangle
rect.set_longueur(8)
rect.set_largeur(3)

# Afficher les nouveaux attributs du rectangle
print("Nouvelle longueur :", rect.get_longueur())
print("Nouvelle largeur :", rect.get_largeur())
