class Insect:

    def __init__(self, especie):
        self.__especie = especie

    def get_especie(self):
        return self.__especie

    def set_especie(self, especie):
        self.__especie = especie
    
    def __str__(self):
        return '{}:{}'.format(self.__class__.__name__, self.get_especie())
