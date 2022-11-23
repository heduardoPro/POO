class Conta:
    def __init__(self, titular, numero, saldo, limite):
        self._titular = titular
        self._numero = numero
        self._saldo = saldo
        self._limite = limite

    def __str__(self):
        return "\nDados da Conta: \nTitular: {} \nNumero: {} \nSaldo: {} \nLimite: {}".format(self._titular, self._numero, self._saldo, self._limite)
    
    def deposita(self, valor):
        self._saldo += valor
        print('\nDeposito realizado! {}'.format(valor))

    def saque(self, valor):
        if(self._saldo < valor):
            print("\nSaldo insuficiente!")
            return False
        else:
            self._saldo -= valor
            print("\nSaque de {}, realizado!".format(valor))
            return True
    
    def transfere_para(self, conta_destino, valor):
        retirou = self.saca(valor)
        if(retirou):
            conta_destino.deposita(valor)
            print("\nTransferência realizada!")
            return True
        else:
            print("\nHouve um problema ao tentar realizar a transferência!")
            return False            

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa
        

class ContaCorrente(Conta):

    def __init__(self, numero, titular, saldo, limite):
        super().__init__(numero, titular, saldo, limite)
    
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2

    def deposita(self, valor):
        self._saldo += valor - 0.10 
    
    def __str__(self):
        return "\nDados da Conta Corrente: \nNumero: {} \nTitular: {} \nSaldo: {} \nLimite: {}".format(self._numero, self._titular, self._saldo, self._limite)

class ContaPoupanca(Conta):

    def __init__(self, numero, titular, saldo, limite):
        super().__init__(numero, titular, saldo, limite)
    
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3

    def __str__(self):
        return "\nDados da Conta Poupança: \nNumero: {} \nTitular: {} \nSaldo: {} \nLimite: {}".format(self._numero, self._titular, self._saldo, self._limite)
