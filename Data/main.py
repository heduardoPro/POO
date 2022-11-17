from data import Data

'''Criação de um objeto data com dados válidos fornecidos pelo usuário'''
data = Data(31, 12, 2022)
print(data)

'''ultizando o metodo diaSeguinte que irá avançar para o dia seguinte, tanto no: dia, mes e ano.'''
data.diaSeguinte()
print(data)

data2 = Data() #Data fornecido pela biblioteca datetime
print(data2)

data2.diaSeguinte()
print(data2)

'''Utilização do método bissexto'''

data3 = Data(15, 12, 2002)
print(data3.bissexto())

d1 = Data()
d2 = Data()
d3 = d1 + d2

print(f"\n<< Primeiro caso: soma de duas datas >>\n{d3}")

"Segundo caso: soma de uma data e um inteiro"
d4 = d1 + 715

"A ordem dos fatores não afetará na execução"
d4 = 1 + d4

print(f"\n<< Segundo caso: soma de uma data e um inteiro >>\n{d4}")