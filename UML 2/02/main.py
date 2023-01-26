from produto import Produto
from item_pedido import ItemPedido
from pedido import Pedido

produto1 = Produto(111, 10.5, 'caneta')
produto2 = Produto(112, 1.5, 'folha')
produto3 = Produto(113, 2.5, 'lapis')

item1 = ItemPedido(produto1, 1)
item2 = ItemPedido(produto2, 2)
item3 = ItemPedido(produto3, 3)

pedido = Pedido(0)

pedido.adicionar_item(item1)
pedido.adicionar_item(item2)
pedido.adicionar_item(item3)

valor_all = pedido.obter_total()
pedido.set_valor_total(valor_all)
print(pedido.get_valor_total())