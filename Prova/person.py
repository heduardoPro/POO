class Person:
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return '{}({})'.format(self.get_nome(), self.get_age())

    def validaIdade(self):
        if (self.__age >= 1 and self.__age <= 150):
            print('Idade Válida.')
        else:
            raise Exception('A idade informada não está no intervalo de [1-150]')
            
    def get_nome(self):
        return self.__name

    def set_nome(self, name):
        self.__name = name

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age
