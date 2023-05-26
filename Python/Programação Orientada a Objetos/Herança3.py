class Forma():
    def __init__(self):
        self.area = 0
        self.perimetro = 0

class Retangulo(Forma):
    def __init__(self):
        super().__init__()

    def calcularArea(self,altura,largura):
        area = altura*largura
        print(area)
    def calcularPerimetro(self,altura,largura):
        print(altura * 2+ largura * 2)
class Triangulo(Forma):
    def __init__(self):
        super().__init__()
    def calcularArea(self,altura,largura):
        area = altura*largura
        print(area)
    def calcularPerimetro(self,altura,largura):
        print(altura * 2+ largura * 2)

triiangulo = Retangulo()
triiangulo.calcularArea(5,5)
triiangulo.calcularPerimetro(5,5)