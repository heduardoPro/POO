from funcionario import Funcionario

class Diretor(Funcionario):
    
    def __init__(self, nome, data_nascimento, salario,):
        super().__init__(nome, data_nascimento, salario)


class Gerente(Funcionario):
    
    def __init__(self, nome, cpf, salario, senha, qtde_gerenciados):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtde_gerenciados = qtde_gerenciados

    def autentica(self, senha):
        if self._senha == senha:
            print('Gerente Autenticado!')
            return True
        else:
            print('Gerente não Autenticado!')
            return False
        
g