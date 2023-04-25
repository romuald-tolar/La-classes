class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

# Instanciation d'un objet Animal
animal1 = Animal()

# Impression de l'attribut age de l'animal
print("Age initial de l'animal :", animal1.age)

# Faire vieillir l'animal et afficher son âge
animal1.vieillir()
print("Age de l'animal après une année :", animal1.age)
