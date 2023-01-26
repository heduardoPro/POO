from produto import Produto

class ItemPedido:

    def __init__(self, produto: Produto, quantidode: int):
        self.__produto = produto
        self.__quantidade = quantidode

    def __str__(self) -> str:
        return (f'Código: {self.produto.get_codigo()}, Valor: {self.produto.get_valor()}, quantidade: {self.__quantidade}')

    def get_produto(self):
        return self.__produto

    def set_produto(self, produto):
        self.__produto = produto
    
    def get_quantidade(self):
        return self.__quantidade

    def set_quantidade(self, quantidade):
        self.__quantidade = quantidade