from nuisance import Nuisance
from insect import Insect

class Mosquito(Insect, Nuisance):

    def __init__(self, especie):
        super().__init__(especie)

    def buzz(self):
        print('{} buzzing around.'.format(self.get_especie()))

    def annoy(self):
        print('buzz buzz buzz')

