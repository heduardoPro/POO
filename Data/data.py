'''Importação da biblioteca datetime'''
import datetime

class Data:
    '''Aplicando o construtor com os atributos iniciais'''
    def __init__(self, dia = datetime.date.today().day, mes = datetime.date.today().month, ano = datetime.date.today().year):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    '''Métodos getters/setters para cada atributo'''
    def get_dia(self):
        return self.__dia

    def set_dia(self, dia):
        self.__dia = dia

    def get_mes(self):
        return self.__mes
        
    def set_mes(self, mes):
        self.__mes = mes

    def get_ano(self):
        return self.__ano

    def set_ano(self, ano):
        self.__ano = ano 
            
    
    def __str__(self):
        return '{}/{}/{}'.format(self.__dia, self.__mes, self.__ano)

    '''Método para avançar a data para o dia seguinte'''
    def diaSeguinte(self):
        '''1° Se a data for 31/12/0000, o dia seguinte será 01/01/0001
           2° Se o mes terminar com 31, ou seja, for ímpar ele passsará pro dia 01 do próximo mes.
           3° Se o mes terminar com 3, ou seja, for par ele passsará pro dia 01 do próximo mes.'''
        if self.__dia <= 31 and self.__ano == 12:
            self.__dia += 1
            self.__mes += 1  
            self.__ano += 1
        elif ((self.__dia == 31 and self.__mes < 12 % 2 != 0)):
            self.__mes += 1
            self.__dia = 1
        elif ((self.__dia == 30 and self.__mes < 12 % 2 == 0)):
            self.__mes += 1
            self.__dia = 1
        else:
            self.__dia += 1

    '''méMtodo para verificar se o ano é bissexto.'''
    def anoBissexto(self):
        '''Se o ano for divisível por 4, 100 e 400 o ano será bissexto, Caso contrário o ano não será bissexto.'''
        if self.__ano % 4 == 0:
            if self.__ano % 100 == 0:
                if self.__ano % 400 == 0:
                    return True
                
                else:
                    return False
            else:
                return False
        else: 
            return False

    def __add__(self, dado):
        pass

