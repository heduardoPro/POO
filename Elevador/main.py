from elevador import Elevador

elevador = Elevador(10, 5)

while(True):
    açao = int(input('\nQual ação voce deseja realizar? \n 1 - Subir: \n 2 - Descer: \n 3 - Entrar: \n 4 - Sair: \n\n '))
    if açao == 1:
        elevador.Subir()
        
    if açao == 2:
        elevador.Descer()
        
    if açao == 3:
        elevador.Entrar()
        
    if açao == 4:
        elevador.Sair()