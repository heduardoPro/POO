from conta import Conta, ContaCorrente, ContaPoupanca

c = Conta('1234', 'Henrique', 0, 2500)
cc = ContaCorrente('4567', 'Eduardo', 0, 3000)
ca = ContaPoupanca('7891', 'Silva', 0, 1000)

cc.deposita(100)
print('foi depositado: ', cc._saldo)

#c.atualixa(0.01)
#cc.atualixa(0.01)
#ca.atualixa(0.01)

print('conta: ', c)
print('Conta Corrente: ', cc)
print('Conta Poupança: ', ca)