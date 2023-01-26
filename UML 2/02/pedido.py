from item_pedido import ItemPedido

class Pedido:

    lista_pedido = []
    
    def __init__(self, valor_total: float) -> None:
        self.valor_total = valor_total

    def get_valor_total(self):
        return self.__valor_total

    def set_valor_total(self, valor):
        self.__valor_total = valor

    def adicionar_item(self, item: ItemPedido):
        self.lista_pedido.append(item)

    def obter_total(self):
        total = 0
        for i in self.lista_pedido:
            qtd = float(i.get_quantidade())
            vlr = float(i.get_produto().get_valor())
            total += (qtd * vlr)
        return total