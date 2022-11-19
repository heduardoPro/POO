from cartaoMensagem import CartaoMensagem

class cartaoNamorados(CartaoMensagem):

    def __init__(self, destiantario, remetente):
        super().__init__(destiantario, remetente)
        self.remetente = remetente

    def __str__(self):
        return ("{}, meu amor! feliz dia dos namorados. Beijos! {}".format(self.destinatario, self.remetente))