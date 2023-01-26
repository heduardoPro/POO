from nuisance import Nuisance
from person import Person

class Telemarketing(Person):

    def __init__(self, name, age):
        super().__init__(name, age)
    
    def giveSalesPitch(self):
        return '{} pressiona os outros a comprar coisas.'.format(self.get_nome())
    
    def annoy(self):
        return '{} irrita ao dar um discurso de vendas'.format(self.get_nome())

