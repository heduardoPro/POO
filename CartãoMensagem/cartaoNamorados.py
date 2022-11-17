from cartao_mensagem import CartaoMensagem

class CartaoNamorados(CartaoMensagem):

    def __init__(self, De, Para):
        super().__init__(De)
        self.Para = Para

    def __str__(self) -> str:
        return (f"Feliz dia dos namorados meu amor, {self.Para}!\nBeijos de {self.De}\n")