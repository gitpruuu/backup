from datas import Data

class Conta:

    def __init__(self, numero, titular, saldo,dt_atual, limite=1000.0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    def extrato(self):
        print("Titular {}\nSaldo R$: {}\nLimite R$: {}".format(self.__titular, self.__saldo, self.__limite))
    
    def deposita(self, valor):
        self.__saldo += valor
    
    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
            print("R$: {} sacado!".format(valor))
        else:
            print("Saldo insuficiente")

    def transfere(self, valor, conta_destino):
        self.saca(valor)
        conta_destino.deposita(valor)

    def __pode_sacar(self, valor):
        valor_disponivel = self.__saldo + self.__limite
        return valor_disponivel >= valor
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property        
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001" 
        
    @staticmethod
    def codigos_bancos():
        return {"banco brasil":"001","caixa":"104","bradesco":"237"}
    

c1 = Conta(123, "Nico", 55.5, 1000.0)

c1.saca(10000)
