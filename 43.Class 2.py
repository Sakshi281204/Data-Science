class Animal:
    def __init__(self,name=None):
        self.name=name
    def Animalname(self):
        print(self.name)
    def info(self):
        print("4 legs")
# an=Animal()
# an.Animalname()
# an.info()
class Human(Animal):
    def Humaninfo(self):
        print("Intelligent")
    def info(self):
        print("Intelligent Organism")
Hu=Human("Ajay")
Hu.Animalname()
Hu.info()
