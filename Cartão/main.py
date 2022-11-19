from cartaoAniversario import CartaoAniversario

listaMsg = []

msg1 = CartaoAniversario('Michael', 'Henrique')
msg2 = CartaoAniversario('Duda', 'Henrique')
msg3 = CartaoAniversario('Aluísio', 'Henrique')

listaMsg.append(msg1)
listaMsg.append(msg2)
listaMsg.append(msg3)

for msg in listaMsg:
    print(msg)