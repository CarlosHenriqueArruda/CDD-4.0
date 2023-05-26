#Classe animal

class Animal():
    def __init__(self,nome,cor):
        self.nome = nome
        self.cor = cor
    def comer(self):
        print(f"O {self.nome} foi comer...")
    def EmitirSom(self):
        print("Fez barulho!")
class Gato(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def EmitirSom(self):
        print(f"O {self.nome} miou!")
class Cachorro(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def EmitirSom(self):
        print(f"O {self.nome} latiu")
class Vaca(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

warwick = Cachorro("Warwick","Cinza")
yummi = Gato("Yummi","Branca")
alistar = Vaca("Alistar","Lilais")

warwick.EmitirSom()
alistar.EmitirSom()