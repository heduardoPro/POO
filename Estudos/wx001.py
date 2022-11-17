class Triangulo:

    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def Calcu_Perimetro(self, soma):
        self.soma = (self.ladoA + self.ladoB + self.ladoC)