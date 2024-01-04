class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, prenom):
        self.prenom = prenom

    def afficherAge(self):
        return f"L'Ã¢ge de l'animal est {self.age} ans"

    def afficherPrenom(self):
        return f"L'animal se nomme {self.prenom}"


animal1 = Animal()
print(animal1.afficherAge())  
animal1.vieillir()
print(animal1.afficherAge())  
animal1.nommer("Luna")
print(animal1.afficherPrenom())