from conta import Conta, ContaCorrente, ContaPoupanca, AtualizadorDeContas

c = Conta('Henrique', 1234, 500, 1000)
cc = ContaCorrente('Demetrios', 6666, 500, 1000000)
cp = ContaPoupanca('Aluisio', 1010, 500, 1000000)

print(c)
print(cc)
print(cp)

c.atualiza(0.01)
cc.atualiza(0.01)
cp.atualiza(0.01)

print(c)
print(cc)
print(cp)
print(c.atualiza)

adc = AtualizadorDeContas(0.01)
adc.roda(c)
adc.roda(cc)
adc.roda(cp)

print("Saldo Total: {}".format(adc._saldo_total))