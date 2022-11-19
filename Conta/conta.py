class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite

    def deposita(self, valor):
            self._saldo += valor

    def saque(self, valor):
        if self._saldo > 0:
            self._saldo -= valor

        else:
            print('Saldo insuficiente!')

    def atualixa(self, taxa):
        self._saldo += self._saldo * taxa
        
    def __str__(self):
        return "Dados da Conta: \nNumero: {} \nTitular: {} \nSaldo: {} \nLimite:{}".format(self._numero, self._titular, self._limite)

class ContaCorrente(Conta):

    def __init__(self, numero, titular, saldo, limite):
        super().__init__(numero, titular, saldo, limite)
    
    def atualixa(self, taxa):
        self._saldo += self._saldo * taxa * 2

    def deposita(self, valor):
        self._saldo += valor - 0.10 

class ContaPoupanca(Conta):

    def __init__(self, numero, titular, saldo, limite):
        super().__init__(numero, titular, saldo, limite)
    
    def atualixa(self, taxa):
        self._saldo += self._saldo * taxa * 3

