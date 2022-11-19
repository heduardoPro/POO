from cartaoMensagem import CartaoMensagem

class CartaoAniversario(CartaoMensagem):

    def __init__(self, destiantario, remetente):
        super().__init__(destiantario, remetente)
        self.remetente = remetente

    def __str__(self):
        return ("{}, Feliz aniversario! te desejo toda felicidade desse mundo. Abraços {}!".format(self.destinatario, self.remetente))