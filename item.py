class Item:
    def __init__(self, produto, preco, quantidade):
        self.produto = produto
        self.preco = preco
        self.quantidade = quantidade

    def calcula_total(self):
        return self.preco * self.quantidade

