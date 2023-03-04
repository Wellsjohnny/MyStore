class Carrinho:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, produto):
        self.produtos.remove(produto)

    def total(self):
        return sum([produto.preco_total for produto in self.produtos])

