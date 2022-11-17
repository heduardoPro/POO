from cartao_mensagem import CartaoMensagem

class CartaoNatal(CartaoMensagem):

    def __init__(self, De, Para):
        super().__init__(De)
        self.Para = Para

    def __str__(self):
        return (f"Olá, {self.Para}!\npor meio desse cartão gostaria de desejar um feliz natal para voce e familia. \nAbraços! \n{self.De}")