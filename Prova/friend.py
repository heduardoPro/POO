from person import Person

class Friend(Person):

    listafriends = []
    contador = 0
    
    def __init__(self, name, age, hobby):
        super().__init__(name, age)
        self.__name = name
        self.__age = age
        self.__hobby = hobby

    def get_nome(self):
        return self.__name

    def set_nome(self, name):
        self.__name = name

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age

    def get_hobby(self):
        return self.__hobby

    def set_hobby(self, hobby):
        self.__hobby = hobby
     
    def chill(self):
        return '{} is chilling.'.format(self.get_nome())

    def __str__(self):
        return '{}({}) {}'.format(self.get_nome(), self.get_age(), self.get_hobby())

    def play(self, listafriends, friend):
        self.listafriends.append(friend)
        if len(listafriends) == 0:
            return 'Jogar'.format(self.get_hobby())
        elif len(listafriends) == 1:
            return 'Jogar {} com {}'.format(self.get_hobby(), listafriends[0])
        elif len(listafriends) == 2:
            return 'Jogar {} com {} e {}'.format(self.get_hobby, listafriends[0], listafriends[1])
        else:
            texto = 'jogando {} com '.format(self.get_hobby())
            texto2 = ''
            
            for amigo in listafriends:
                if contador == len(listafriends) - 1:
                    texto2 += '{}'.format(amigo)
                else:
                    texto2 += '{}, '.format(amigo)
                    contador += 1
            return texto + texto2

    def __eq__(self, other):
        if self.get_nome() == other.get_nome() and self.get_age() == other.get_age() and self.get_hobby() == other.get_hobby():
            return True
        else:
            return False