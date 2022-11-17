class CartaoMensagem:

    listaMsg = []

    def __init__(self, De):
        self.De = De
        self.listaMsg.append(self)

    def ExibirMsg(self):
        for msg in self.listaMsg:
            print(msg)

    def get_Destinatario(self):
        return self.De

    def set_Destinatario(self, De):
        self.De = De