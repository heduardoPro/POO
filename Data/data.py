from datetime import date, timedelta

class Data:
    '''quando a data não for inicializada no construtor, é inserida a data de hoje'''
    def __init__(self, dia = date.today().day, mes = date.today().month, ano = date.today().year):

        '''Verificação de datas válidas'''

        if mes > 0 and mes <=12:
            self.__mes =  mes

        if ano > 0:
            self.__ano = ano
        
        if( mes in (1, 3, 5, 7, 8, 10, 12) and dia <= 31):
            self.__dia = dia

        elif( mes in (4, 6, 9, 11) and (dia <=30)):
            self.__dia = dia

        elif (mes == 2):
            if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 and dia <=29:
                self.__dia = dia
            else:
                self.__dia = dia
        
        else:
            print('Data inválida')

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

     
                
    def bissexto(self):

        '''metodo que verifica se o ano é bissexto'''

        if (self.__ano % 4 == 0 and self.__ano % 100 != 0) or (self.__ano % 400 == 0):
            print('Ano bissexto')
        else:
            print('O ano não é bissexto')

    def diaSeguinte(self):
        '''
        metodo que avança a data em 1 dia:

        31/12  incrementa ano, mes = 1 (janeiro)
        bissexto dia 29, incrementa mês e dia = 1
        dia 28 incrementa mês e dia = 1
        meses com 30 dias incrementa mês e dia = 1
        meses com 31 dias incrementa mês e dia = 1
        o restante das datas incrementa 1 dia'''

        if (self.__mes == 12 and self.__dia == 31):
            self.__dia = 1
            self.__mes = 1
            self.__ano +=1

        elif (self.__mes in (1, 3, 5, 7, 8, 10) and self.__dia == 31):
            self.__dia = 1
            self.__mes += 1
        
        elif (self.__mes == 2) and (self.__ano % 4 == 0 and self.__ano % 100 != 0 or self.__ano % 400 == 0 ):
            if self.__dia == 29:   
                self.__dia = 1
                self.__mes += 1

            elif self.__dia == 28:
                self.__dia += 1

        elif (self.__mes == 2 and self.__ano % 4 != 0 and self.__ano % 100 == 0 or self.__ano % 400 != 0 and self.__dia == 28):
            self.__dia = 1
            self.__mes += 1
        
        elif (self.__mes in (4, 6, 9, 11) and (self.__dia) == 30):
            self.__dia = 1
            self.__mes += 1

        else:
            self.__dia += 1

    '''Metodo que retorna a data como string'''
    def __str__(self):
        return ('Data: {}/{}/{}'.format(self.__dia, self.__mes, self.__ano))
