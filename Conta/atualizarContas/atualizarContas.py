from conta import Conta

class AtualizadorDeContas(Conta):
    
    def __init__(self, selic, saldo_total = 0):
        self._selic = selic
        self._saldo_total = saldo_total

    def roda(self, conta):
    print("Saldo da Conta: {}".format(self._saldo))
    self._saldo_total += conta.atualiza(self._selic)
    print("Saldo Final: {}".format(self._saldo_total))