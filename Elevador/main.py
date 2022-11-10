from elevador import Elevador

elevador = Elevador(int(input('Quantidade de andares: ')), int(input('Capacidade máxima do elevador: ')))

while(True):
    açao = int(input('\nQual ação voce deseja realizar? \n 1 - Subir: \n 2 - Descer: \n 3 - Entrar: \n 4 - Sair: \n\n '))
    if açao == 1:
        elevador.Subir()
        break
    if açao == 2:
        elevador.Descer()
        break
    if açao == 3:
        elevador.Entrar()
        break
    if açao == 4:
        elevador.Sair()
        break