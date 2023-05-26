#Classe ingresso


class Ingresso():
    def __init__(self,valor):
        self.valor = valor
    def imprimir_valor(self):  #metodo
        print(f'Valor do ingresso normal: {self.valor}')
        return self.valor
class VIP(Ingresso):
    def __init__(self,valor):
        super().__init__(valor)
    def imprimir_valor(self,porcentagem):
        total = self.valor+(porcentagem*self.valor/100)
        print(f'Valor do ingresso VIP: {total}')
        

ingresso1 = Ingresso(100)
ingresso = VIP(50)
ingresso1.imprimir_valor()
ingresso.imprimir_valor(50)
