class Student:
    def __init__(self, nom, prenom, numero_etudiant, credits=0):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = credits
    
    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
    
    def get_credits(self):
        return self.__credits
john_doe = Student("Doe", "John", 145)
john_doe.add_credits(10)
john_doe.add_credits(20)
john_doe.add_credits(-5)  # cette ligne n'aura pas d'effet sur le nombre de crédits de John Doe
print(john_doe.get_credits())  # affiche 30
