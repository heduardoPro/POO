from datetime import datetime

class Pessoa:

    def __init__(self, nome: str, sexo: chr, data_nasc: int):
        self.__nome = nome
        self.__sexo = sexo
        self.__data_nasc = data_nasc

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome
    
    def get_sexo(self):
        return self.__sexo

    def set_sexo(self, sexo):
        self.__sexo = sexo
    
    def get_data_nasc(self):
        return self.__data_nasc

    def set_data_nasc(self, data_nasc):
        self.__data_nasc = data_nasc

    def __str__(self):
        return 'Nome: {} \nSexo: {} \nData de nascimento: {}'.format(self.__nome, self.__sexo, self.__data_nasc)

class Aluno(Pessoa):

    def __init__(self, nome: str, sexo: chr, data_nasc: int, matricula: int):
        super().__init__(nome, sexo, data_nasc)
        self.__matricula = matricula

    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, matricula):
        self.__matricula = matricula

    def __str__(self):
        return 'Nome: {} \nSexo: {} \nData de nascimento: {} \nMatricula: {}'.format(self.get_nome(), self.get_sexo(), self.get_data_nasc(), self.get_matricula())

class Ator(Pessoa):
    class Contrato:

        def __init__(self, comeco: int, fim: int, salario: int):
            self.comeco = comeco
            self.fim = fim
            self.salario = salario

        def __str__(self):
            return 'Comeco do contrato: {} \nFim do contrato: {} \nSalário: {}'.format(self.comeco, self.fim, self.salario)

    def __init__(self, nome: str, sexo: chr, data_nasc: int, comeco, fim, salario):
        super().__init__(nome, sexo, data_nasc)
        self.__contrato = self.Contrato(comeco, fim, salario)

    def get_contrato(self):
        return self.__contrato

    def set_contrato(self, contrato):
        self.__contrato = contrato
    def __str__(self):
        return 'Nome: {} \nSexo: {} \nData de nascimento: {} \n{}'.format(self.get_nome(), self.get_sexo(), self.get_data_nasc(), self.get_contrato())

class Personagem(Ator):

    def __init__(self, nome: str, sexo: chr, data_nasc: int, comeco: int, fim: int, salario: int, caracterizacao: str, novela: str):
        super().__init__(nome, sexo, data_nasc, comeco, fim, salario)
        self.__caracterizacao = caracterizacao
        self.__novela = novela

    def get_caracterizacao(self):
        return self.__caracterizacao

    def ser_caracterizacao(self, caracterizacao):
        self.__caracterizacao = caracterizacao

    def get_novela(self):
        return self.__novela

    def set_novela(self, novela):
        self.__novela = novela
    
    def __str__(self):
        return 'Nome: {} \nSexo: {} \nData de nascimento: {} \n{} \nCaracterização: {} \nNovela: {}'.format(self.get_nome(), self.get_sexo(), self.get_data_nasc(), self.get_contrato(), self.__caracterizacao, self.__novela)
