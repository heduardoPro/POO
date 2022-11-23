from conta import Conta, ContaCorrente, ContaPoupanca

c = Conta('1234', 'Henrique', 0, 2500)
cc = ContaCorrente('4567', 'Eduardo', 0, 3000)
ca = ContaPoupanca('7891', 'Silva', 0, 1000)

c.deposita(100)
cc.deposita(500)
ca.deposita(1000)

print(c)
print(cc)
print(ca)

cc.atualiza(0.01)
print('\nSaldo da conta corrente atualizado: ', ca._saldo)
ca.atualiza(0.01)
print('\nSaldo da conta poupança atualixado: ', ca._saldo)