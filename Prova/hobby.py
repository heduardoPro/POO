from enum import Enum

class Hobby(Enum):
    music = 1
    sports = 2
    games = 3

    def my_hobby(hobby):
        if hobby == Hobby.sports:
            print('Meu hobby é ', hobby.name)
        else:
            print('O hobby não é sports e sim ', hobby.name)