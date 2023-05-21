#Primeira classe criada, aprendendo Programação orientada a objetos.
#Nesse exercicio eu criei a minha primeira classe, uma pessoa,a prendi a adicionar atributos, verificar se são
# compatives, orientar cada atributo e otimizar funções.
class Pessoa: #Nome da classe
    #Criando nova classe "Pessoa"
    #definindo Metodos/caracteristicas abaixo
    def __init__(self,nome,peso,idade,comendo=False,falando=False): #array
        # adicionando uma variavel para cada metodo
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.comendo=comendo
        self.falando=falando
        #printando
        print(f"{nome}, {peso}kg, {idade} Anos.")
    def Comer(self,comida):
        #nova função Comer
        #adicionado a função de não comer se estiver falando
        #novo objeto comida
        self.comida = comida
        if self.comendo ==False and self.falando == False:
            print(f"{self.nome} Começou a comer {comida}!")
            self.comendo = True
        elif self.comendo == False and self.falando == True:
            print(f"{self.nome}, é feio comer enquanto fala! (não pode comer)")
        elif self.comendo == True:
            print(f"{self.nome} Já está comendo!")
    def PararDeComer(self):
        #nova função Parar de comer
        if self.comendo:
            print(f"{self.nome} Parou de comer.")
            self.comendo = False
        else:
            print("Não estava comendo.")
    def Falar(self):
        #nova função Falar
        #novo objeto Falar
        if self.comendo == True:
            print(f"{self.nome}, você não pode falar de boca cheia!")
        else:
            print(f"{self.nome} Começou a falar!")
            self.falando = True
    def PararDeFalar(self):
        #nova função Parar de falar
        if self.falando == True:
            print(f"{self.nome} Parou de falar.")
            self.falando = False
        else:
            print("Não estava falando.")
    #função utilizada para printar todas as informações sobre a pessoa
    def __str__(self):
        return f"{self.nome}, {self.peso}kg, {self.idade} anos, Comendo: {self.comendo}"
