class Pedido:
    def __init__(self, cliente, carrinho):
        self.cliente = cliente
        self.carrinho = carrinho

    def resumo(self):
        return f'Pedido de {self.cliente.nome} - Total: R$ {self.carrinho.total():.2f}'