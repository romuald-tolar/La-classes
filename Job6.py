class Animal:
    def nommer(self, nom):
        self.prenom = nom

animal1 = Animal()

animal1.nommer("Maximax")
print("L'animal se nomme  :", animal1.prenom)
