class Conta:
    def __init__(self, titular, numero, saldo, limite):
        self._titular = titular
        self._numero = numero
        self._saldo = saldo
        self._limite = limite

    def __str__(self):
        return "\nDados da Conta: \nTitular: {} \nNumero: {} \nSaldo: {} \nLimite: {}".format(self._titular, self._numero, self._saldo, self._limite)
    
    def deposito(self, valor):
        if valor > 0:
            self._saldo += valor
            print('\nDeposito realizado! {}'.format(valor))

        else:
            print('\nvalor inválido!')
            return False

    def saque(self, valor):
        if self._saldo < valor:
            print("\nSaldo insuficiente!")
            return False
        else:
            self._saldo -= valor
            print("\nSaque de {}, realizado!".format(valor))
            return True           

    #def atualiza(self, taxa):
    #   self._saldo += self._saldo * taxa
        
    def atualiza(self):
        return self._saldo

class ContaCorrente(Conta):

    def __init__(self, numero, titular, saldo, limite):
        super().__init__(numero, titular, saldo, limite)
    
    #def atualiza(self, taxa):
    #   self._saldo += self._saldo * taxa * 2
    def atualiza(self):
        return self._saldo

    def deposita(self, valor):
        self._saldo += valor - 0.10 
    
    def __str__(self):
        return "\nDados da Conta Corrente: \nNumero: {} \nTitular: {} \nSaldo: {} \nLimite: {}".format(self._numero, self._titular, self._saldo, self._limite)

class ContaPoupanca(Conta):

    def __init__(self, numero, titular, saldo, limite):
        super().__init__(numero, titular, saldo, limite)
    
    #def atualiza(self, taxa):
    #    self._saldo += self._saldo * taxa * 3
    def atualiza(self):
        return self._saldo

    def __str__(self):
        return "\nDados da Conta Poupança: \nNumero: {} \nTitular: {} \nSaldo: {} \nLimite: {}".format(self._numero, self._titular, self._saldo, self._limite)

class AtualizadorDeContas(Conta):
    def __init__(self, selic, saldo_total = 0):
        self._selic = selic
        self._saldo_total = saldo_total

    def roda(self, conta):
        print("Saldo da Conta: {}".format(conta))
        self._saldo_total += conta.atualiza(self._selic)
        print("Saldo Final: {}".format(self._saldo_total))