import datetime
class Data:

    def __init__(self, dia, mes, ano):
        if dia == 0:
            dia = datetime.today().day
        self.__dia = dia
        if mes == 0:
            mes = datetime.today().month
        self.__mes = mes
        if ano == 0:
            ano = datetime.today().year
        self.__ano = ano

        def get_dia(self):
            return self.__dia

        def set_dia(self, dia):
            self.__dia = dia

        def get_mes(self):
            return self.__mes
        
        def set_mes(self, mes):
            self.__mes = mes

        def get_ano(self):
            return self.ano

        def set_ano(self, ano):
            self.__ano = ano

        def diaSeguinte(self):
            if self.__dia == 30 and self.__mes == 12:
                self.__ano += 1
                self.__dia = 1
                self.__mes = 1
            
            elif self.__mes == 2:
                if self.bissexto() and self._-dia == 29:
                    self.__mes += 1
                    self.__dia = 1
                
                elif (not self.bissexto() and self.__dia == 28):
                    self.__mes += 1
                    self.__dia = 1

        def bissexto(self):
            if self.__ano % 4 == 0:
                if self.__ano % 100 == 0:
                    if self.__ano % 400 == 0:
                        return True
                    else:
                        return False
                else:
                    return True
            else:
                return False     
            

    def __str__(self):
        return '{}/{}/{}'.format(self.__dia, self.__mes, self.__ano)
