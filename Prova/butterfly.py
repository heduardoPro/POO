from insect import Insect

class Butterfly(Insect):

    __colorslist = []
    
    def __init__(self, especie, colors, butterfly = None):
        super().__init__(especie)
        self.__colorslist.append(colors)

    def get_colorslist(self):
        return self.__colorslist

    def set_colorslist(self, colors):
        self.__colorslist = colors

    def get_colors(self):
        return self.__colors

    def set_colors(self, colors):
        self.__colors = colors

    def get_butterfly(self):
        return self.__butterfly

    def set_butterfly(self, butterfly):
        self.__butterfly = butterfly

    def __str__(self):
        return '{}{}'.format(self.get_especie(), self.get_colorslist())
    