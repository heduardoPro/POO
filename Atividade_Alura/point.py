class Elevador:

    def __init__(self, andarAtual, totalAndares, capaciadadeMax, pessoasDentro):
        self.andarAtual = andarAtual
        self.totalAndares = totalAndares
        self.capaxidadeMax = capaciadadeMax
        self.pessoasDentro = pessoasDentro

    def icializar(self, capacidadeMax, totalAndares):
        if self.andarAtual == 0:
            print('O elevador já está no terreo')
            return True
        else:
            print('O elevador não esta no terreo, está no {}° andar'.format(self.andarAtual))



elevador = Elevador(0, 5, 8, 0)
print(elevador.andarAtual())