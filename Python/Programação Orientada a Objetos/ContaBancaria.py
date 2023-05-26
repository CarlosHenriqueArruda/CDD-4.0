class ContaBancaria:
    def __init__(self,numero,nome,tipo):
        self.numero = int(numero)
        self.saldo = 0
        self.nome = nome
        self.tipo = tipo
        self.status = False
        self.limite = 0
        self.limitetotal = self.saldo + self.limite

    ##### METODO ATIVAR #####
    def ativar (self):
        if self.status == False:
            self.status = True
            print("Sua conta agora está ativada!")
        else:
            print("Sua conta já está ativada.")

    ##### METODO LIMITE #####
    def limite(self):
        if self.status == True:
            print(self.limite)
            return self.limite
    def adicionar_limite(self, limiteadicionar):
        if self.status == True:
            self.limite += limiteadicionar
            return self.limite
    def sacar_limite(self,sacarlimite):
        if self.status == True and self.limite >= sacarlimite:
            limiteatualizado =  self.limite - sacarlimite
            print(f"Você sacou R${sacarlimite}, seu limite atual é de {limiteatualizado}")
            return limiteatualizado
        else:
            print("Sua conta está desativada, ative-a para ter acesso as funções.")


    ##### METODO DEPOSITO #####
    def depositar(self,deposito):
        if self.status == True:
            if self.limiteatualizado < self.limite:
                resto = self.limiteatualizado + deposito

        elif self.status == True:
            print(f"Seu deposito foi de R${deposito}, o saldo atual da sua conta é R${self.saldo}")
            return self.saldo
        else:
            print("Sua conta está desativada, ative-a para ter acesso as funções.")

    ##### METODO SACAR #####
    def sacar(self,valorsacado):
        saque = self.saldo - valorsacado
        return saque

    ##### METODO VERIFICAR SALDO #####
    def verif_saldo(self,verificador):
        print(self.saldo)