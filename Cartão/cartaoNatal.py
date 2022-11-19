from cartaoMensagem import CartaoMensagem

class CartaoNatal(CartaoMensagem):

    def __init__(self, destiantario, remetente):
        super().__init__(destiantario, remetente)
        self.remetente = remetente
        
    def __str__(self):
        return ("Há quanto tempo velho amigo {}, por meio dessa carta quero te dejesar um feliz natal \
                 para voce e sua familia! Do seu amigo {}".format(self.destinatario, self.remetente))