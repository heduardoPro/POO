import datetime

class JogadorFutebol:

    def __init__(self, nome, posicao, nascimento, nacionalidade, altura, peso):
        self.__nome = nome
        self.__posicao = posicao
        self.__nascimento = nascimento
        self.__nacionalidade = nacionalidade
        self.__altura = altura
        self.__peso = peso

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome
    
    def get_posicao(self):
        return self.__posicao

    def set_posicao(self, posicao):
        self.__posicao = posicao

    def get_nascimento(self):
        return self.__nascimento

    def set_nascimento(self, nascimento):
        self.__nascimento = nascimento

    def get_nacionalidade(self):
        return self.__nacionalidade

    def set_macionalidade(self, nacionalidade):
        self.__nacionalidade = nacionalidade

    def get_altura(self):
        return self.__altura

    def set_altura(self, altura):
        self.__altura = altura

    def get_peso(self):
        return self.__peso

    def set_peso(self, peso):
        self.__peso = peso

    def calcularIdade(self):
        hoje = datetime.datetime.now()
        idade = hoje.year - self.__nascimento.year - ((hoje.month, hoje.day) < (self.__nascimento.month, self.__nascimento.day))
        return idade

    def calcularAposentar(self):
        if self.get_posicao() == "defesa":
            if self.__idade >= 40:
               print("Já está aposentado")
            else:
               print("você se aposentará em {} anos".format(40-self.__idade))
        if self.get_posicao() == "meio campo":
            if self.__idade >= 38:
                 print("Já está aposentado")
            else:
                print("você se aposentará em {} anos".format(38-self.__idade))
        if self.get_posicao() == "atacante":
            if self.__idade >= 35:
                 print("Já está aposentado")
            else:
                print("você se aposentará em {} anos".format(35-self.__idade))
    def __str__(self) :
        return "Nome do jogador: %s, Posição: %s, Data de Nascimento: %s, Nacionalidade: %s, Altura: %f, Peso: %d" % \
                (self.__nome, self.__posicao, self.__nascimento, self.__nacionalidade, self.__altura, self.__peso)

jogador = JogadorFutebol('Eduardo', 'atacante', datetime.date(2002, 12, 15), 'brasileiro', 1.80, 90)
jogador.calcularAposentar()
print(jogador)