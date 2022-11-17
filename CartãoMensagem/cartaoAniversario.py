from cartao_mensagem import CartaoMensagem

class CartaoAniversario(CartaoMensagem):

    def __init__(self, De, Para):
        super().__init__(De)
        self.Para = Para

    def __str__(self):
       return (f"Digníssimo(a), {self.Para}, Quero te desejar um feliz aniversário e tudo de bom!\n Abaços! \n{self.De}")