class Student:
    def __init__(self, nom, prenom, numero_etudiant, credits=0):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = credits
        self.__level = self.__studentEval()
    
    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__studentEval()
    
    def get_credits(self):
        return self.__credits
    
    def studentInfo(self):
        print(f"Nom: {self.__nom}")
        print(f"Prénom: {self.__prenom}")
        print(f"Identifiant: {self.__numero_etudiant}")
        print(f"Niveau: {self.__level}")
    
    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"
john_doe = Student("Doe", "John", 145)
john_doe.add_credits(85)
john_doe.studentInfo()
